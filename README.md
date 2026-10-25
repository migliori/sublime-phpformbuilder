# PHP Form Builder — Sublime Text Autocompletions

[![](https://img.shields.io/badge/PHP%20Form%20Builder-7.0-blue)](https://www.phpformbuilder.pro)
[![](https://img.shields.io/badge/Sublime%20Text-3%20%7C%204-orange)](https://www.sublimetext.com)
[![](https://img.shields.io/badge/Package%20Control-available-green)](https://packagecontrol.io/packages/PHP%20Form%20Builder)

Autocompletions for [**PHP Form Builder**](https://www.phpformbuilder.pro "PHP Form Builder"),
the PHP framework to build Bootstrap 4, Bootstrap 5, Bulma, Foundation, Material, Tailwind and UIkit forms —
sold directly on [phpformbuilder.pro](https://www.phpformbuilder.pro).

> **Updated for PHP Form Builder v7.0** — all methods, arguments and plugin names are up to date.

## Features

* **62 completions** covering the full PHP Form Builder API: form creation, inputs, selects, checkboxes, radios, buttons, file uploads, plugins, rendering and static helpers
* Access all completions with a single shortcut
* Access completions from the Sublime Text menu
* Standard auto-completion while you type
* Ready-to-use form template snippet

## Installing

### With Package Control (recommended)

1. [Install Package Control](https://packagecontrol.io/installation) if not already done
2. Open the command palette: `ctrl+shift+p` (`super+shift+p` on macOS)
3. Type `Package Control: Install Package` and press Enter
4. Search for `PHP Form Builder` and press Enter

### Without Git

Download the latest source from [GitHub](https://github.com/migliori/sublime-phpformbuilder) and copy the folder to your Sublime Text `Packages` directory.

### With Git

Clone the repository in your Sublime Text `Packages` directory:

```bash
git clone https://github.com/migliori/sublime-phpformbuilder.git "PHP Form Builder"
```

The `Packages` directory is located at:

| OS      | Path                                                        |
|---------|-------------------------------------------------------------|
| macOS   | `~/Library/Application Support/Sublime Text/Packages/`      |
| Linux   | `~/.config/sublime-text/Packages/`                          |
| Windows | `%APPDATA%/Sublime Text/Packages/`                          |

## Usage

### Shortcut

Press `ctrl+alt+w` (`super+alt+w` on macOS) to open the quick panel with all available completions.

### Auto-completion

Start typing the name of a PHP Form Builder function — the auto-complete list will appear.

Or type `phpformbuilder` to show all available completions.

### Menu

`Tools → PHP Form Builder → Completions`

### Custom shortcut

The default shortcut is `ctrl+alt+w` (`super+alt+w` on macOS).

You can change it in `Preferences → Package Settings → PHP Form Builder → Key Bindings`.

## More

PHP Form Builder is also available in the [PHP CRUD Generator](https://www.phpcrudgenerator.com) package —
a web app that generates a PHP MySQL Bootstrap admin dashboard using a visual user interface.
