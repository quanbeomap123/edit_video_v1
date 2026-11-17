# Delivery and cleanup

## Handoff

Deliver the MP4, exact project/timeline name, native-versus-rendered text limits and retained source locations. Keep word timings, edit maps, font/license records and special-motion source. Never label a HyperFrames render a CapCut export or imply unobserved UI playback.

Check dimensions/fps, duration/frame count, codec, decode errors and audio presence. Inspect decoded final frames, especially talking-head/asset/typo transitions. Validate native references including the imported-media bin. Store full reports on disk; summarize briefly. Do not rerun renders/checks after unrelated documentation-only changes.

For upload advice, verify current official platform requirements at that time. The working output is usually 1080×1920 H.264 MP4 / 30 fps. Upscaling low-resolution source or inventing frames does not restore detail. Preserve the original file during transfer. Posting requires separate authorization.

## Reusable library

One asset root contains SFX, fonts, backgrounds, motion source, style references and project-specific originals. Catalogue relative paths, source paths/URLs, hashes, sizes and usage/license notes. Retain licenses privately. Do not package licensed Windows fonts in a redistributable skill. User-supplied memes/reference videos are not automatically licensed stock.

Verify/reuse catalogue files before downloading again. Preserve newer project entries when updating an older catalogue. Shared tools/models are reusable infrastructure, not per-project cache. Media files stay outside this skill package.

## Final-only cleanup

Preserve versions during editing. After the user identifies the final, keep:

- Approved final MP4 and editable final CapCut timeline.
- Every required media/bin reference, alpha graphic, voice/SFX, font and editable source.
- Original footage, especially the only remaining copy when a Downloads original disappeared.
- Reusable assets/licenses, shared runtimes/models and a small audit/metadata snapshot.

Retire obsolete exports, old timelines/draft copies and generated project caches only after proving they are outside the keep set. Folder names such as `old`, `temp` or `backup` are not evidence of disposability. Preserve user edits. Prune unused material definitions/bin entries before deleting corresponding files.

1. Resolve the final version from user decision/project state. If ambiguous, finish inventory and ask before dependent deletion.
2. Derive the keep set from actual final documents, media bin, other-project references and library catalogue. Hash the final MP4 and snapshot metadata. Archive reusable code/inputs before removing old folders.
3. Produce explicit absolute deletion targets, protected paths and estimated size. Before recursive deletion/move on Windows verify targets remain within the intended workspace or explicitly named project directory; never delete an unchecked computed root.
4. Stop only task-owned preview servers holding locks, preferably using their CLI stop. If needed verify PID/command/start identity first; never kill all Node/Python processes or CapCut. Track partial completion and retry only remaining authorized targets.
5. Commit final-only metadata without racing the app. Preserve final ID/track content and active/root mirrors. Remove only planned unreferenced files.
6. Recheck final hash, references/bin, catalogue paths, root mirrors and the single intended home entry. Report actual reclaimed space or label estimates. A tiny metadata snapshot is an audit aid, not a guarantee that deleted media can be restored.

Never rerun one project's cleanup script against a new project. Ground a new plan in current documents. The bundled validator is intentionally read-only; this skill ships no automatic deletion command.
