# Contributing / 参与方式

Thanks for your interest in Moqi.

This repository is primarily a portfolio prototype. It is open for reading, discussion and lightweight contributions, but it is not yet a packaged consumer product.

## Good Contribution Areas

- README or documentation improvements.
- Broken link or typo fixes.
- Suggestions for clearer AI product / HRI interaction logic.
- Validation scenario suggestions.
- Safer privacy, memory or interaction-boundary design ideas.

## Current Boundaries

- The full system requires a local sensing side, cloud backend and purchased robot hardware.
- Private server addresses, tokens, real desktop logs and personal memory data are not part of the public repository.
- The robot hardware is an off-the-shelf kit; hardware design and third-party firmware follow their original licenses.

## Before Opening an Issue

Please include:

- What you expected to see.
- What you actually saw.
- The page or document path involved.
- Screenshots when the issue is visual.

## Local Preview

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```
