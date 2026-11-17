# Design and sound

## Composition

Study references with full-video contact sheets and dense strips around hooks, title entrances and cuts. Separate observed devices from guesses about fonts, SFX and timing. Do not claim to have heard audio when only measurements/frames were available.

Compose around faces, gestures and asset focal points. Useful arrangements: large names above the speaker, small lead-ins with larger keywords, short left-aligned phrases near the lower picture area, captions beneath memes. Keep a layout coherent through a thought rather than changing position every phrase. Check phone-size readability and platform-safe placement. When a caption overlaps an asset scene in time, keep it clear of the asset's important content.

Verify Vietnamese glyphs at final size. Bold sans is the main subtitle voice; thin serif/light italic gives selected contrast. Fit lines using real font measurements. Highlights identify important words/numbers, not every word. Start with neutral white and limited red plus one topic-appropriate accent; do not universalize one video's brand color. No glass panels or heavy glow. Use subtle shadow and, occasionally, a faint selected-keyword glow. Keep rights/license records privately, not as visible production labels.

## Typography motion

Choose motion by role: decisive hook, restrained explanation, expressive emphasis and a clean landed ending. Titles settle and hold. Avoid floating/pulsing text loops, identical entrances everywhere and random effects every phrase.

The user's four recipes are choices, not a checklist:

1. **Word reveal:** position + opacity, sequenced to spoken words.
2. **Character settle:** position + scale + opacity, eased with a short character stagger.
3. **Tracking burst:** compressed characters expand with scale/rotation/opacity. In seek-based HTML renders animate per-character x, not `letterSpacing`, which reflows and may stutter.
4. **Layered emphasis:** opacity envelope separate from inner scale/rotation/blur; sharpen quickly into a readable hold.

Use NFC-normalized Vietnamese and grapheme-safe splitting, e.g. `Intl.Segmenter`. Never split an accent from its base letter. Use absolute word time and local subcomposition time correctly. Give groups an exact end gate; do not fade the last word while it is entering.

Use native CapCut text/keyframes for ordinary captions/simple reveals. For selected rendered scenes preserve HTML/JS, timing, fonts and licenses. Verify actual alpha support. Tell the user CapCut edits these as media clips rather than text.

## Pace, transitions and audio

Keep the edit/tempo map and word timings canonical. Remap picture, captions and SFX together after trims or speed changes. Vary pace smoothly, preserve important pauses and use subtle formant-preserved pitch only when useful. Do not copy the previous video's pitch/rate values mechanically.

Use motivated cuts/punch-ins, brief directed image entrances, mask reveals or a short dip at selected changes. Energy does not require transitions on every cut.

Reuse documented local SFX first. A hashed CapCut cache filename establishes neither sound identity nor usage rights. Do not bypass access to its online catalogue. If needed, download a suitable free library from an authoritative source and retain its license/source. The existing Kenney Interface Sounds library is CC0 and supplies short UI/foley cues, not a complete cinematic/meme collection. Paid generation requires authorization for its cost.

Place sparse impacts/clicks/swishes/reveals on meaningful events. Keep dialogue dominant and independent native SFX clips. Do not add sound to every word. Audition with visuals when supported.

Measure loudness/true peak and clipping. Around -17 to -16 LUFS with -2 to -1 dBTP headroom is a starting target here, not a TikTok requirement. Fix filter-induced duration changes at sample level; check sync at separated speech windows. Disclose when sound was measured but not subjectively heard.

## Feedback without rebuilding every scene

Keep a scene manifest with scene ID, timeline start/duration, render input hash, output path and editable source. Render only affected scene clips when timing is unchanged, then replace those clips in the existing timeline after a metadata snapshot/concurrency check. If duration changes, remap dependent downstream timing and affected scenes. Changes to global styling, canvas/fps or voice timing may invalidate many cached scenes. Producing a new final MP4 generally still requires exporting the full timeline; reuse unchanged rendered scenes. Do not promise range rendering when the selected renderer lacks it.
