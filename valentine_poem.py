#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║   Valentine's Day Poem Generator for Shruthi from Tharun     ║
║   ─────────────────────────────────────────────────────────   ║
║   Creates an original, heartfelt poem with South Indian       ║
║   imagery, prints it to the console, and generates an         ║
║   elegant animated HTML page saved as                         ║
║   'valentine_for_shruthi.html'.                               ║
╚═══════════════════════════════════════════════════════════════╝

Author  : THARUN
For     : SHRUTHI ❤️
Requires: Python 3 (standard library only)
"""

import os
import sys

# Fix Windows console encoding so emoji prints correctly
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

# ─────────────────────────────────────────────────────────────
# 1.  THE POEM  –  6 stanzas, AABB rhyme, simple heartfelt
#     English with South Indian cultural imagery
# ─────────────────────────────────────────────────────────────

POEM_TITLE = "My Eternal Love for You, Shruthi"
POEM_SUBTITLE = "Happy Valentine's Day — From THARUN, with all my heart"

STANZAS = [
    # Stanza 1 — Jasmine & first sight
    (
        "Like jasmine blooming in the morning dew,\n"
        "My whole world changed the day I found you.\n"
        "Your smile is brighter than the temple lamp at night,\n"
        "You turned my ordinary days into something bright."
    ),
    # Stanza 2 — Monsoon rains & comfort
    (
        "When the monsoon rains would fall upon our lane,\n"
        "Your gentle voice would wash away my every pain.\n"
        "Like kolam drawn at dawn with patience and with care,\n"
        "You painted love in corners I forgot were there."
    ),
    # Stanza 3 — Imaginary future moments together
    (
        "I dream of sitting with you on a terrace watching stars,\n"
        "Sharing filter coffee, forgetting all our scars.\n"
        "One day I'll hear your laughter in the evening breeze,\n"
        "And all these dreams I carry now will finally find their ease."
    ),
    # Stanza 4 — Gratitude & support
    (
        "You held my hand when I was lost and could not see,\n"
        "You whispered, 'I believe in you,' and set me free.\n"
        "No temple bell could ring as sweetly as your name,\n"
        "Since you walked into my life, nothing is the same."
    ),
    # Stanza 5 — Deep love & devotion
    (
        "Like the river Kaveri that flows and never ends,\n"
        "My love for you, Shruthi, forever bends and bends.\n"
        "You are the turmeric thread that ties me to this life,\n"
        "My blessing, my companion, my joy beyond all strife."
    ),
    # Stanza 6 — Eternal vow
    (
        "So hear me now, my love, this promise that I make —\n"
        "I'll stand beside you every step for both our sakes.\n"
        "Through every season, every sunrise, every prayer,\n"
        "I'm yours, Shruthi — today, tomorrow, everywhere."
    ),
]

FOOTER_MESSAGE = "Forever yours, THARUN ❤️"


# ─────────────────────────────────────────────────────────────
# 2.  CONSOLE OUTPUT — beautifully formatted preview
# ─────────────────────────────────────────────────────────────

def print_poem():
    """Print the poem with decorative borders to the console."""
    width = 62
    border = "═" * width

    print()
    print(f"  ╔{border}╗")
    print(f"  ║{'':^{width}}║")
    print(f"  ║{'💝  ' + POEM_TITLE + '  💝':^{width}}║")
    print(f"  ║{POEM_SUBTITLE:^{width}}║")
    print(f"  ║{'':^{width}}║")
    print(f"  ╠{border}╣")

    for i, stanza in enumerate(STANZAS):
        print(f"  ║{'':^{width}}║")
        for line in stanza.split("\n"):
            display = line[:width].center(width)
            print(f"  ║{display}║")
        if i < len(STANZAS) - 1:
            print(f"  ║{'~ ~ ~':^{width}}║")

    print(f"  ║{'':^{width}}║")
    print(f"  ║{FOOTER_MESSAGE:^{width}}║")
    print(f"  ║{'':^{width}}║")
    print(f"  ╚{border}╝")
    print()


# ─────────────────────────────────────────────────────────────
# 3.  HTML GENERATION — reads the standalone animated HTML file
# ─────────────────────────────────────────────────────────────

def generate_html() -> str:
    """Return the full HTML string for the animated Valentine page.

    The HTML is maintained as a standalone file (valentine_for_shruthi.html)
    for easy editing. If the file already exists we simply read it.
    """
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "valentine_for_shruthi.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()

    # Minimal fallback
    stanzas_html = ""
    for idx, stanza in enumerate(STANZAS):
        delay = 1.0 + idx * 2.5
        lines_html = "<br>".join(stanza.split("\n"))
        stanzas_html += (
            f'<div style="animation-delay:{delay}s;">\n'
            f'  <p>{lines_html}</p>\n'
            f'</div>\n'
        )
    return (f"<html><body><h1>{POEM_TITLE}</h1>"
            f"{stanzas_html}<p>{FOOTER_MESSAGE}</p></body></html>")


# ─────────────────────────────────────────────────────────────
# 4.  SHARING INSTRUCTIONS
# ─────────────────────────────────────────────────────────────

def print_instructions(filepath: str):
    """Print clear instructions on viewing and sharing the HTML."""
    abs_path = os.path.abspath(filepath)
    print("=" * 64)
    print("  🌹  HOW TO VIEW & SHARE THIS VALENTINE'S POEM  🌹")
    print("=" * 64)
    print()
    print("  ➊  VIEW LOCALLY")
    print(f"     • Double-click the file to open in your browser:")
    print(f"       {abs_path}")
    print(f"     • Or run:  start {filepath}")
    print()
    print("  ➋  SHARE VIA GITHUB GIST  (recommended — free, permanent)")
    print("     1. Go to  https://gist.github.com")
    print("     2. Sign in with a GitHub account.")
    print("     3. Paste the contents of 'valentine_for_shruthi.html'")
    print("        into the editor, name the file 'valentine_for_shruthi.html'.")
    print("     4. Click 'Create public gist'.")
    print("     5. Prepend the raw URL with  https://htmlpreview.github.io/?")
    print("        to get a live-rendered link you can share.")
    print()
    print("  ➌  SHARE VIA NETLIFY DROP  (free, instant, 24-hour link)")
    print("     1. Go to  https://app.netlify.com/drop")
    print("     2. Drag & drop 'valentine_for_shruthi.html' (or a folder")
    print("        containing it) onto the page.")
    print("     3. Copy the generated URL and send it to Shruthi! 💌")
    print()
    print("  ➍  SHARE VIA TIINY.HOST  (free, custom link, 7-day hosting)")
    print("     1. Go to  https://tiiny.host")
    print("     2. Upload 'valentine_for_shruthi.html'.")
    print("     3. Choose a cute link name (e.g., shruthi-valentine).")
    print("     4. Share the link! 🎉")
    print()
    print("  ➎  SHARE VIA SURGE.SH  (free, permanent, command-line)")
    print("     1. Install Surge:  npm install --global surge")
    print("     2. Create a folder, copy the HTML inside, then run:")
    print("        surge ./your-folder  shruthi-valentine.surge.sh")
    print("     3. Share the URL with Shruthi! 🌷")
    print()
    print("=" * 64)
    print("  💝  Happy Valentine's Day, Shruthi!  💝")
    print("=" * 64)
    print()


# ─────────────────────────────────────────────────────────────
# 5.  MAIN
# ─────────────────────────────────────────────────────────────

def main():
    print("\n🌹  Generating your Valentine's Day poem for Shruthi …\n")

    # ── Print poem to console ──
    print_poem()

    # ── Generate & save HTML ──
    html_content = generate_html()
    output_file = "valentine_for_shruthi.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"  ✅  HTML file saved → {os.path.abspath(output_file)}")
    print()

    # ── Print sharing instructions ──
    print_instructions(output_file)


if __name__ == "__main__":
    main()
