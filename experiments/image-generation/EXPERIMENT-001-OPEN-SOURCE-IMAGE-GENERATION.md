# Experiment 001 — Open-Source Image Generation

**Status:** DISCOVER / SCREEN
**Category:** Image Generation
**Purpose:** Systematic evaluation of open-source and locally runnable image-generation tools for the DÉJÀ-VU 3 production stack.

## Evaluation pipeline

DISCOVER → SCREEN → TEST → EVALUATE → DECIDE → INTEGRATE

## Decision states

- 🟢 ADOPT — approved for integration
- 🟡 TEST — requires hands-on validation
- 🔵 WATCH — promising, not currently prioritized
- 🟣 BUILD — candidate for an in-house workflow/component
- 🔴 REJECT — not suitable
- ⚪ ARCHIVE — retained for reference

## Initial shortlist

| Project / Model | Primary role | Initial status | Notes |
|---|---|---|---|
| ComfyUI | Workflow / orchestration | 🟢 ADOPT | Central local production environment candidate |
| FLUX.2 Klein 4B | Image generation + editing | 🟢 ADOPT | High-priority first production test |
| Qwen Image | Text rendering + image generation/editing | 🟢 ADOPT | High priority for posters and typography |
| SDXL | General image generation / ecosystem | 🟢 ADOPT | Large model and LoRA ecosystem |
| SD3.5 | Modern image generation | 🟡 TEST | Quality and hardware comparison |
| ControlNet | Structural control | 🟢 ADOPT | Pose, depth, edges and composition |
| IP-Adapter | Image references | 🟢 ADOPT | Reference-driven generation |
| LoRA | Style / character adaptation | 🟢 ADOPT | Required for custom DÉJÀ-VU 3 style and characters |
| Real-ESRGAN | Upscaling | 🟢 ADOPT | Lightweight finalization tool |
| SUPIR | Restoration / upscale | 🟡 TEST | Higher-quality but more demanding |
| InstantID | Identity preservation | 🟡 TEST | Character / face consistency |
| PuLID | Identity preservation | 🟡 TEST | Character / face consistency |
| PhotoMaker | Multi-reference identity | 🟡 TEST | Character experiments |
| Z-Image | Efficient generation | 🟡 TEST | Local speed candidate |
| Hunyuan Image | Advanced generation | 🟡 TEST | Strong technical candidate; license must be checked per model |
| HiDream | Image generation | 🟡 TEST | Secondary quality candidate |
| PixArt | Image generation | 🔵 WATCH | Research / secondary ecosystem |
| Lumina | Image generation | 🔵 WATCH | Research candidate |
| Chroma | Image generation | 🔵 WATCH | Research candidate |
| InvokeAI | Local creative environment | 🟡 TEST | Alternative to ComfyUI |
| Krita AI Diffusion | AI-assisted editing | 🟡 TEST | Creative editing environment |
| Fooocus | Simplified generation UI | 🔵 WATCH | Useful for rapid experiments |
| AUTOMATIC1111 | Stable Diffusion UI | 🔵 WATCH | Large legacy extension ecosystem |

## Screening criteria

1. License and commercial-use terms
2. Repository activity and maintenance
3. Hardware requirements
4. Local/offline feasibility
5. Image quality
6. Prompt adherence
7. Text rendering
8. Image editing / inpainting
9. Reference-image support
10. Character consistency
11. 9:16 / portrait workflow suitability
12. ComfyUI compatibility
13. Automation/API potential
14. Security and dependency risks
15. Reproducibility

## DÉJÀ-VU 3 target workflow

ComfyUI → model → LoRA / IP-Adapter / ControlNet → image editing → upscaling → 1080×1920 → TikTok / PDF export.

## Next tests

- Confirm available GPU/VRAM and system RAM.
- Install ComfyUI in an isolated environment.
- Run FLUX.2 Klein 4B baseline test.
- Run Qwen Image baseline test.
- Compare SDXL and SD3.5 against the same prompts.
- Record generation speed, VRAM usage, quality and failure modes.
- Verify licenses from official model repositories before commercial use.

## Rule

No model is considered commercially approved solely because its repository is public or open source. The exact license of the selected model/checkpoint and its dependencies must be verified before production integration.
