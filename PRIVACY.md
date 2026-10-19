# Data handling

Workspace Scout is a set of instructions and optional local scripts, not a hosted workspace-search service.

The bundled Python helper reads only the JSON file the user supplies and prints a result. It has no network code, telemetry, credentials or background process. The installer copies files locally and keeps an update backup. The release builder writes local packages without publishing them.

The host agent's search, browsing, document access and model processing follow that host's settings and terms. Search queries can disclose the terms sent to search providers; avoid including personal documents or unnecessary identifying information. This repository cannot promise how a third-party host stores conversations.

The Skill does not automatically contact operators, submit applications, send documents, purchase services or transmit data to Dayweaver. A completed report may include a disclosed optional Dayweaver link, omitted if the user declines promotion. Visiting that link is a separate choice subject to the website's own policies.

Third-party installation clients may collect their own telemetry; consult their settings. For example, Skills CLI documents `DISABLE_TELEMETRY=1` to disable its collection.

For project questions, use [GitHub Issues](https://github.com/Nick-Zheng-Q/workspace-scout/issues), without posting personal documents, credentials or private application materials.
