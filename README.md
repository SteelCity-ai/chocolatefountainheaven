# Chocolate Fountain Heaven redesign

Seven-page client-review draft for Paperclip STE-299, based on https://www.chocolatefountainheaven.com/ and its original photographs/content.

Edit `site/` directly. It is a static site with no build step or new package dependencies. Serve that directory with an existing HTTP server. The existing Hermes preview uses port 4179; Mike's temporary local tunnel is http://127.0.0.1:4189.

Read `DESIGN.md` for the implemented design direction and `RECOVERY.md` for the original recovery. Extracted `*.html.txt` files retain source content for comparison. `build_pages.py` is the historical bootstrap and is disabled because regenerating would overwrite the reviewed pages.

`qa-browser.sh` uses the already-installed gstack browser for responsive and keyboard checks. Set `BROWSE_STATE_FILE` to a dedicated state file and pass the base URL as its first argument. No browser installation is required.

The inquiry form opens an email draft; it does not send inquiries itself. This work is ready for review, not an approved production release. Confirm client facts/prices and approve publication separately.

For future changes, save a Git checkpoint before extended visual review. Limit each agent turn to a bounded change, reuse the installed browser, and report the pushed SHA plus remaining checks. The two prior Hermes runs reached Paperclip's 1800-second timeout while iterating on QA; retrying the entire assignment repeats that failure.
