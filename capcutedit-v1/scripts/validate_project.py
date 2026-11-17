"""Read-only checks for local JSON CapCut drafts. Python standard library only."""
import argparse
import json
import re
from pathlib import Path


def validate(project):
    root = Path(project).resolve()
    result = {"ok": False, "project": str(root), "timelines": [],
              "media_paths_checked": 0, "media_bin_paths_checked": 0,
              "errors": [], "notes": [], "playback_verified": False}

    def error(code, **details):
        result["errors"].append({"code": code, **details})

    def read(path):
        try:
            obj = json.loads(path.read_text(encoding="utf-8-sig"))
            if not isinstance(obj, dict):
                raise ValueError("Expected JSON object")
            return obj
        except (OSError, ValueError, UnicodeError) as exc:
            error("unreadable_json", file=str(path), detail=str(exc))
            return None

    def check_path(raw, context, bucket):
        if not isinstance(raw, str) or not raw.strip():
            return
        result[bucket] += 1
        if re.match(r"^https?://", raw, re.I):
            result["notes"].append({"code": "remote_media_not_verified", "path": raw})
            return
        expanded = re.sub(r"^##_draftpath_placeholder_[^/\\]+_##", str(root).replace("\\", "/"), raw)
        file = Path(expanded)
        if not file.is_absolute():
            file = root / file
        if not file.is_file():
            error("missing_media", context=context, path=raw, resolved=str(file.resolve()))

    def document(path, expected_id=None):
        doc = read(path)
        if doc is None:
            return None
        if expected_id and doc.get("id") != expected_id:
            error("timeline_id_mismatch", file=str(path), expected=expected_id, actual=doc.get("id"))
        mats, tracks = doc.get("materials"), doc.get("tracks")
        if not isinstance(mats, dict) or not isinstance(tracks, list):
            error("unsupported_schema", file=str(path), detail="materials object and tracks array required")
            return doc
        ids = {m["id"] for values in mats.values() if isinstance(values, list)
               for m in values if isinstance(m, dict) and "id" in m}
        for track in tracks:
            for seg in track.get("segments", []):
                mid = seg.get("material_id")
                if mid and mid not in ids:
                    error("unresolved_material_id", file=str(path), track=track.get("name"), material_id=mid)
                span = seg.get("target_timerange")
                if isinstance(span, dict):
                    start, duration = span.get("start"), span.get("duration")
                    if not isinstance(start, (int, float)) or not isinstance(duration, (int, float)) or start < 0 or duration <= 0:
                        error("invalid_segment_range", file=str(path), segment_id=seg.get("id"))
        for kind in ("videos", "audios"):
            for mat in mats.get(kind, []):
                check_path(mat.get("path"), str(path), "media_paths_checked")
        mirror = path.parent / "template-2.tmp"
        if mirror.exists():
            other = read(mirror)
            if other is not None and other != doc:
                error("timeline_mirror_mismatch", file=str(mirror))
        return doc

    pjfile = root / "Timelines" / "project.json"
    rootfile = root / "draft_content.json"
    if not rootfile.exists() and (root / "draft_info.json").exists():
        rootfile = root / "draft_info.json"
    if pjfile.exists():
        pj = read(pjfile)
        if pj is not None:
            active = pj.get("main_timeline_id")
            timelines = pj.get("timelines", [])
            if not isinstance(timelines, list) or not timelines:
                error("unsupported_schema", file=str(pjfile), detail="nonempty timelines array required")
                timelines = []
            listed = [t.get("id") for t in timelines if isinstance(t, dict)]
            if len(set(listed)) != len(listed):
                error("duplicate_timeline_id", file=str(pjfile))
            if active not in listed:
                error("active_timeline_not_listed", id=active)
            active_doc = None
            for timeline in timelines:
                tid = timeline.get("id")
                if not isinstance(tid, str) or not tid or Path(tid).name != tid or tid in {".", ".."}:
                    error("invalid_timeline_id", id=tid)
                    continue
                doc = document(root / "Timelines" / tid / "draft_content.json", tid)
                result["timelines"].append({"id": tid, "name": timeline.get("name"), "active": tid == active})
                if tid == active:
                    active_doc = doc
            main = document(rootfile)
            if main is not None and active_doc is not None and main != active_doc:
                error("root_active_mismatch", root=str(rootfile), active=active)
    else:
        doc = document(rootfile)
        if doc is not None:
            result["timelines"].append({"id": doc.get("id"), "name": doc.get("name"), "active": True})

    meta_path = root / "draft_meta_info.json"
    if meta_path.exists():
        meta = read(meta_path)
        if meta is not None:
            for group in meta.get("draft_materials", []):
                for item in group.get("value", []):
                    raw = item.get("file_Path") or item.get("file_path") or item.get("path")
                    check_path(raw, str(meta_path), "media_bin_paths_checked")
    else:
        result["notes"].append({"code": "media_bin_metadata_absent", "file": str(meta_path)})
    result["ok"] = not result["errors"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = validate(args.project)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
