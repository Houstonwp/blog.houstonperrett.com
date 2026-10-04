# Houston Perrett's blog

Source for https://blog.houstonp.com/.

## Build and check

Use **Hugo extended 0.167.0**, Go **1.27.1**, and Python **3.12+**. Hugo/Go obtain the theme version pinned in `go.mod` and verified by `go.sum`.

```sh
hugo --gc --minify
python scripts/check_site.py
hugo server
```

Netlify uses the build command, runtime pin, and `public` output in `netlify.toml`. GitHub Actions builds and checks without deploying; its Hugo installer verifies the official archive checksum. Go is needed for Hugo Modules, not for running a blog backend.

The Beautiful Hugo theme remains pinned to `v0.0.0-20260706190448-b2d547f7a61c`. The available 5.2.0 release changes its asset pipeline, removes jQuery, and adds build-time network dependencies for self-hosted assets. That larger migration is deliberately separate from this small maintenance pass. Review its [upgrade guide](https://github.com/halogenica/beautifulhugo/blob/v5.2.0/.agents/skills/upgrade-beautiful-hugo/resources/v5.1-to-v5.2.md) before updating the module. The existing theme currently warns about deprecated `.Page.IsNode` on Hugo 0.167.0.

## Publishing and feeds

Production builds exclude drafts. The July 2026 article remains `draft: true`; preview it privately with `hugo server --buildDrafts` and do not pass `--buildDrafts` in production. Publishing or rewriting that article is an editorial decision.

Both `/index.xml` and the legacy `/rss.xml` are intentionally generated. Each contains only the latest **one** published item, controlled by `services.rss.limit`. The custom RSS layouts preserve these URLs and their format-specific self links. Do not delete the legacy output or change the item limit as routine cleanup.

`static/_redirects` preserves the legacy blog domain and the old `/subscribe` link. DNS/domain aliases must be configured by the hosting provider for domain redirects to apply.

## Verification limits

`python scripts/check_site.py` checks local links/assets throughout generated HTML, homepage metadata, both one-item XML feeds, draft exclusion, and legacy redirects. External-link crawling and visual checks are separate. One archived article contains an X/Twitter shortcode that fetches remote oEmbed data during the build; restricted networks may warn and omit that embedded tweet. The rest of the build succeeds, but that warning is not a successful verification of the remote embed.

## Browser checks

CI also installs the pinned Playwright test dependency from `requirements-test.txt`, checks 320/390/768/1280px layouts for horizontal overflow and broken images, and saves screenshots as the `site-previews` artifact. The resume check also produces Letter/A4 PDFs for human print review; generating a PDF alone is not a visual pagination approval. Run locally with:

```sh
python -m pip install -r requirements-test.txt
python -m playwright install chromium
python scripts/check_render.py
```
