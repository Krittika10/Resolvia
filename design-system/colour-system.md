
# Resolvia — Colour System

Version: 1.0
Design identity: Engineering Control Room

## 1. Design principles

- Use colour to communicate meaning.
- Keep large surfaces visually quiet.
- Reserve Signal Amber for important interface highlights.
- Use semantic colours for issue status and priority.
- Maintain consistent visual identity across light and dark themes.

## 2. Light Theme

| Token | Hex | Purpose |
|---|---|---|
| Background | #EEEDE6 | Main workspace |
| Surface | #FAF9F4 | Panels |
| Elevated Surface | #FFFFFF | Floating elements |
| Sidebar | #E6E5DC | Navigation |
| Primary Text | #202521 | Main content |
| Secondary Text | #686D66 | Supporting content |
| Muted Text | #858B82 | Metadata |
| Border | #D4D4CB | Component borders |
| Divider | #C9C9BF | Section separation |
| Accent | #815A16 | Readable amber text |
| Accent Surface | #F3E5C8 | Selected elements |

## 3. Dark Theme

| Token | Hex | Purpose |
|---|---|---|
| Background | #111613 | Main workspace |
| Surface | #19211C | Panels |
| Elevated Surface | #202824 | Floating elements |
| Sidebar | #171E19 | Navigation |
| Primary Text | #F1F1E9 | Main content |
| Secondary Text | #A2AAA2 | Supporting content |
| Muted Text | #7E887F | Metadata |
| Border | #39423B | Component borders |
| Divider | #2D3730 | Section separation |
| Accent | #D9A441 | Active indicators |
| Accent Surface | #3A3020 | Selected elements |

## 4. Signature Colour

Signal Amber: #D9A441

Use for:
- Active navigation indicator
- Current selection
- Important interface highlights
- Selected timeline markers

Do not use as a general background colour.

## 5. Semantic Colours

### Critical Priority
- Light: #A8332A
- Dark: #F18B82

### High Priority
- Light: #8A4B12
- Dark: #F3B26B

### Medium Priority
- Light: #806317
- Dark: #E2C56B

### Low Priority
- Light: #525B54
- Dark: #B7C0B8

### Resolved Status
- Light: #23734C
- Dark: #73C99A

### Neutral Status
- Light: #626B64
- Dark: #A2AAA2

## 6. Issue Status Mapping

| Status | Visual treatment |
|---|---|
| Open | Neutral |
| In Progress | Signal Amber |
| Resolved | Green |
| Closed | Neutral |

## 7. Usage Rules

1. Do not apply Signal Amber to every button or label.
2. Avoid decorative gradients.
3. Never communicate issue status through colour alone.
4. Maintain sufficient text and background contrast.
5. Use the same semantic meaning in both themes.
6. Keep borders subtle and surfaces distinguishable.
