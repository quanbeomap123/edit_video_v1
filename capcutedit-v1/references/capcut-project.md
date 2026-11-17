# Native project handling

## Actual schema first

Inspect a locally created draft and installed CapCut version before writing. Downloaded/template drafts can be non-JSON/encrypted: report unsupported formats rather than inventing a decoder. A helper such as pycapcut is not proof of universal compatibility.

Usual local Windows root: `%LOCALAPPDATA%/CapCut/User Data/Projects/com.lveditor.draft`. Resolve the actual location in a different environment.

For multi-timeline projects, `Timelines/project.json` lists timelines and `main_timeline_id`; documents live under `Timelines/<id>/`. The root document represents the active timeline. Project ID, timeline ID and home-entry draft ID can differ. Preserve their observed roles rather than assigning one UUID everywhere.

## Mutation procedure

1. Snapshot metadata/hash relevant documents; inspect user changes since the previous revision.
2. Prepare in a workspace copy. New timeline IDs/material IDs must be remapped consistently across references.
3. Append within the existing project; update timeline pointers/layout and active root mirrors. Preserve older/user-edited timelines until finalization.
4. Copy media to stable resources; content-hash deduplication is useful. Keep canonical reusable assets in the asset library. Never move/delete a live source.
5. Compare source hashes again before committing; reread/merge if changed. Use atomic replacements when supported.

CapCut can overwrite external changes from its in-memory home index while open. Prepare the complete change first. If closure is necessary, explain the reason and ask the user to save/close the app; never kill CapCut or drive its UI. Commit after closure, then reread. Do not repeatedly fight a live writer. Restoring a missing file at an existing reference can often work without metadata changes/closure.

## Required reference checks

- Each timeline's video/audio `path`, plus segment material IDs.
- Imported-media bin: `draft_meta_info.json` → `draft_materials[*].value[*].file_Path`. Even unused bin entries can trigger missing-media dialogs.
- Resolve `./Resources/...` against the project root. Resolve `##_draftpath_placeholder_<id>_##/Resources/...` against that root before checking existence; it is not a literal folder. Preserve recognized placeholders unless a real repair requires change.
- Active/root JSON and existing `template-2.tmp` mirrors. A live autosave mismatch requires concurrency handling, not automatic overwriting.
- Other-project references before deleting shared media or old draft directories.

Run the read-only bundled validator. A pass does not establish codec/effect compatibility or CapCut playback. Verify separately where supported, otherwise disclose the limit.

## Missing-media repair

Identify the exact failing reference. If media moved into hash-named Shared resources while the bin kept its old name, remap the bin consistently or restore a byte-identical alias at the expected path. Aliases are less invasive while the app is open. Match source candidates by hash/metadata, not extension alone. Back up metadata before rewriting paths and recheck the bin plus all timelines afterward.
