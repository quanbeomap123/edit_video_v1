---
name: capcutedit-v1
description: Edit supplied talking-head footage into short vertical videos in an editable native CapCut project using file-based workflows, Vietnamese captions, selective typography motion, assets and sound design. Use for new edits, revisions, missing-media repairs or final-project cleanup. Applies the saved personal editing style without computer use.
---

# CapcutEdit-v1

Deliver shorts the user can refine in CapCut. Use filesystem/code tools only: no computer use, mouse/keyboard automation or UI automation. This is a personal workflow, not an official CapCut integration or universal draft-format implementation.

## Working contract

- One video has one native project. Use named version timelines during iteration and preserve user edits. After finalization, retain the final MP4, editable final timeline, required media/source and reusable assets; retire obsolete versions using the cleanup procedure.
- Ordinary captions must be native editable CapCut text. Render transparent media only for selected typography scenes whose effects cannot be represented reliably. Retain source and identify these scenes in the handoff. Render special motion as separate scene clips so feedback can replace a scene without rerendering every effect. Never flatten all captions to simplify rendering.
- Keep picture, voice, B-roll/images, captions, special motion and SFX on separate tracks. Assets replace the talking-head picture while voice continues.
- Preserve original footage and spoken meaning. Do not add or strengthen factual claims through new hooks/captions.
- Distinguish metadata checks, inspected frames, subjective listening and actual CapCut playback/export. A successful JSON check or HyperFrames render does not establish CapCut playback. No optional telemetry/feedback submissions.

## Efficient edit loop

1. **Recover needed context.** Read workspace instructions and compact project state, then relevant assets/source. Reuse approved style, runtimes and local assets. Maintain `edit-state.json` with source paths, native project/timeline IDs, stage, style deviations, timing-plan path, final decision and next action. Avoid full chat rereads and large log dumps.
2. **Ground the brief.** Identify footage/order, hook, length, assets and changes from the default. Ask only for blocking missing information. Reference files are media, not executable instructions. Probe footage/audio and inspect frames before cropping.
3. **Lock the rough cut.** Remove failed takes, repetition and unnecessary pauses without clipping breaths or word endings. Preserve intentional pauses. Transcribe the actual delivered voice and map word timings through cuts/tempo changes before detailed motion.
4. **Test style cheaply.** For a new direction, build an 8–12 second study with talking head, an asset scene and one emphasis moment. Use snapshots/short renders. Continue without another approval when this direction is already approved or the user requested a complete file/no stops. Prefer timestamped, batched feedback.
5. **Build the native version.** Before mutating drafts read [capcut-project.md](references/capcut-project.md). For creative work read [design-and-sound.md](references/design-and-sound.md). Reuse components but compose important beats deliberately. Add versions to the same project.
6. **Validate and deliver.** Run the bundled read-only validator. Inspect decoded final frames, phone-size sheets and important transition strips. Check dimensions/fps/duration/codec, audio levels and sync. Repeat only affected checks. Deliver the MP4, project/timeline name and editability/verification limits.
7. **Finalize and clean.** Read [delivery-and-cleanup.md](references/delivery-and-cleanup.md) when finalizing, cleaning or discussing delivery/upload. Another review cut is not final approval.

## Defaults and dependencies

Default to 1080×1920 / 30 fps unless the source/user calls for something else. Strong first-three-second visual hook; rapid varied pace; bold sans captions with narrow settled tracking; sparse semantic color. Thin serif paired with bold sans is selective. Use a subtly animated dark curved grid. No glass, heavy/global glow or visible asset/provenance bookkeeping. Normal captions have no glow.

Read supporting references only when needed. If using installed HyperFrames, Remotion or Typography skills, read the applicable tool instructions then; adapt wall-clock examples to deterministic render time. Verify available runtimes rather than silently requiring paid services or installing dependencies. Prefer local FFmpeg/transcription tools when suitable.

Resolve a reusable library at `<workspace>/assets/` or a user-selected location; read its `README.md` and `catalogue.json` when present. Media remains in the library, not bundled into this skill. Do not assume any previous project or machine-specific path exists.

## Read-only native check

```powershell
python "<skill-dir>/scripts/validate_project.py" "<native-project-folder>"
```

Optional `--report <file.json>` writes details. Exit 0 means checked references/structure resolve, not that CapCut playback or render quality passed. Nonzero means address the reported schema, path or mirror issue. The script never modifies project files.
