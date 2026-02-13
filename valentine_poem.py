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
import textwrap
import datetime

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
    # Stanza 3 — Shared moments & family warmth
    (
        "We sat on that old terrace watching crows fly home,\n"
        "Sharing filter coffee, knowing we would never be alone.\n"
        "Your amma's laughter echoing through the evening breeze,\n"
        "These simple little moments put my restless heart at ease."
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
            # Pad or truncate to fit inside the box
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
# 3.  HTML GENERATION — animated, romantic, South Indian–themed
# ─────────────────────────────────────────────────────────────

def generate_html() -> str:
    """Return the full HTML string for the animated Valentine page."""

    # Build stanza HTML blocks with staggered animation delays
    stanzas_html = ""
    for idx, stanza in enumerate(STANZAS):
        delay = 1.0 + idx * 2.5  # seconds between each stanza reveal
        lines_html = "<br>".join(stanza.split("\n"))
        stanzas_html += (
            f'<div class="stanza" style="animation-delay:{delay}s;">\n'
            f'  <p>{lines_html}</p>\n'
            f'</div>\n'
        )

    html = textwrap.dedent(f"""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Eternal Love for You, Shruthi – Happy Valentine's Day from THARUN</title>
    <meta name="description" content="A heartfelt Valentine's Day poem from Tharun to Shruthi, adorned with South Indian imagery and love.">

    <!-- Google Font — warm, handwritten feel -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">

    <style>
    /* ── ROOT VARIABLES ── */
    :root {{
      --saffron: #E8913A;
      --deep-saffron: #C2621A;
      --rose: #D14D72;
      --deep-rose: #A3284A;
      --lotus-pink: #F2A6C0;
      --leaf-green: #3B7A3B;
      --cream: #FFF8F0;
      --gold: #D4A843;
      --dark-text: #3C1518;
      --petal-start: rgba(255, 182, 193, 0.85);
      --petal-end: rgba(255, 105, 135, 0.7);
    }}

    /* ── RESET & BASE ── */
    *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}

    body {{
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      font-family: 'Cormorant Garamond', 'Georgia', serif;
      color: var(--dark-text);
      overflow-x: hidden;

      /* Gradient background inspired by South Indian sunrise tones */
      background: linear-gradient(
        160deg,
        #FFF5EB 0%,
        #FFE4D6 20%,
        #FDDDE6 40%,
        #FCEAE8 60%,
        #FFF0DB 80%,
        #F2FFE5 100%
      );
      background-attachment: fixed;
    }}

    /* ── RANGOLI SUBTLE PATTERN OVERLAY ── */
    body::before {{
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        radial-gradient(circle at 15% 25%, rgba(232,145,58,0.06) 0%, transparent 50%),
        radial-gradient(circle at 85% 75%, rgba(209,77,114,0.06) 0%, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(59,122,59,0.04) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0;
    }}

    /* ── FLOATING HEARTS CONTAINER ── */
    .hearts-bg {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }}

    .heart {{
      position: absolute;
      bottom: -60px;
      font-size: 1.4rem;
      opacity: 0;
      animation: floatUp linear infinite;
    }}

    @keyframes floatUp {{
      0%   {{ transform: translateY(0) rotate(0deg) scale(0.8); opacity: 0; }}
      10%  {{ opacity: 0.7; }}
      90%  {{ opacity: 0.5; }}
      100% {{ transform: translateY(-110vh) rotate(360deg) scale(1.2); opacity: 0; }}
    }}

    /* ── PETAL PARTICLES ── */
    .petal {{
      position: absolute;
      bottom: -40px;
      width: 14px;
      height: 18px;
      border-radius: 50% 0 50% 50%;
      background: linear-gradient(135deg, var(--petal-start), var(--petal-end));
      opacity: 0;
      animation: petalFloat linear infinite;
    }}

    @keyframes petalFloat {{
      0%   {{ transform: translateY(0) rotate(0deg) translateX(0); opacity: 0; }}
      10%  {{ opacity: 0.6; }}
      50%  {{ transform: translateY(-55vh) rotate(180deg) translateX(40px); }}
      90%  {{ opacity: 0.3; }}
      100% {{ transform: translateY(-112vh) rotate(360deg) translateX(-30px); opacity: 0; }}
    }}

    /* ── MAIN CONTAINER ── */
    .container {{
      position: relative;
      z-index: 1;
      max-width: 720px;
      width: 92%;
      margin: 0 auto;
      padding: 40px 20px 60px;
    }}

    /* ── GIFT-BOX REVEAL ENVELOPE ── */
    .envelope {{
      background: rgba(255,255,255,0.55);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1.5px solid rgba(212,168,67,0.35);
      border-radius: 24px;
      padding: 50px 40px;
      box-shadow:
        0 8px 32px rgba(194,98,26,0.08),
        0 2px 8px rgba(209,77,114,0.06),
        inset 0 1px 0 rgba(255,255,255,0.7);
      animation: envelopeOpen 1.8s ease-out forwards;
      transform-origin: top center;
    }}

    @keyframes envelopeOpen {{
      0%   {{ opacity: 0; transform: scale(0.85) rotateX(15deg); }}
      60%  {{ opacity: 1; transform: scale(1.02) rotateX(-2deg); }}
      100% {{ opacity: 1; transform: scale(1) rotateX(0deg); }}
    }}

    /* ── TITLE ── */
    .title {{
      text-align: center;
      margin-bottom: 12px;
      animation: fadeSlideDown 2s ease-out forwards;
      opacity: 0;
    }}

    .title h1 {{
      font-family: 'Caveat', cursive;
      font-size: clamp(2rem, 5.5vw, 3.2rem);
      font-weight: 700;
      color: var(--deep-rose);
      line-height: 1.2;
      text-shadow: 0 2px 8px rgba(209,77,114,0.12);
    }}

    .title .subtitle {{
      font-size: clamp(0.95rem, 2.5vw, 1.15rem);
      font-style: italic;
      color: var(--deep-saffron);
      margin-top: 8px;
    }}

    /* ── DECORATIVE DIVIDER ── */
    .divider {{
      text-align: center;
      margin: 30px 0;
      font-size: 1.3rem;
      color: var(--gold);
      letter-spacing: 8px;
      animation: fadeIn 2.5s ease-out forwards;
      opacity: 0;
    }}

    /* ── STANZAS ── */
    .stanza {{
      text-align: center;
      margin: 28px 0;
      opacity: 0;
      animation: stanzaReveal 2s ease-out forwards;
    }}

    .stanza p {{
      font-size: clamp(1.05rem, 2.8vw, 1.28rem);
      line-height: 2;
      color: var(--dark-text);
      letter-spacing: 0.02em;
    }}

    @keyframes stanzaReveal {{
      0%   {{ opacity: 0; transform: translateY(30px); filter: blur(4px); }}
      100% {{ opacity: 1; transform: translateY(0);  filter: blur(0);   }}
    }}

    @keyframes fadeSlideDown {{
      0%   {{ opacity: 0; transform: translateY(-20px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes fadeIn {{
      0%   {{ opacity: 0; }}
      100% {{ opacity: 1; }}
    }}

    /* ── STANZA SEPARATOR ── */
    .stanza-sep {{
      text-align: center;
      color: var(--lotus-pink);
      font-size: 1.1rem;
      letter-spacing: 6px;
      margin: 10px 0;
      opacity: 0;
      animation: fadeIn 1.5s ease-out forwards;
    }}

    /* ── FOOTER ── */
    .footer {{
      text-align: center;
      margin-top: 40px;
      padding-top: 20px;
      border-top: 1px solid rgba(212,168,67,0.25);
      animation: fadeIn 3s ease-out forwards;
      animation-delay: {1.0 + len(STANZAS) * 2.5 + 1.5}s;
      opacity: 0;
    }}

    .footer p {{
      font-family: 'Caveat', cursive;
      font-size: clamp(1.4rem, 3.5vw, 1.9rem);
      color: var(--deep-rose);
    }}

    .footer .glowing-heart {{
      display: inline-block;
      font-size: 2rem;
      animation: heartbeat 1.4s ease-in-out infinite;
      filter: drop-shadow(0 0 8px rgba(209,77,114,0.5));
    }}

    @keyframes heartbeat {{
      0%, 100% {{ transform: scale(1); }}
      14%      {{ transform: scale(1.2); }}
      28%      {{ transform: scale(1); }}
      42%      {{ transform: scale(1.15); }}
      56%      {{ transform: scale(1); }}
    }}

    /* ── LOTUS CORNER MOTIFS ── */
    .lotus-corner {{
      position: fixed;
      font-size: 2.5rem;
      opacity: 0.12;
      pointer-events: none;
      z-index: 0;
    }}
    .lotus-tl {{ top: 18px; left: 18px; }}
    .lotus-tr {{ top: 18px; right: 18px; transform: scaleX(-1); }}
    .lotus-bl {{ bottom: 18px; left: 18px; transform: scaleY(-1); }}
    .lotus-br {{ bottom: 18px; right: 18px; transform: scale(-1); }}

    /* ── RESPONSIVE ── */
    @media (max-width: 520px) {{
      .envelope {{ padding: 30px 18px; }}
      .stanza p {{ line-height: 1.85; }}
    }}
    </style>
    </head>
    <body>

    <!-- Lotus corner motifs -->
    <div class="lotus-corner lotus-tl">🪷</div>
    <div class="lotus-corner lotus-tr">🪷</div>
    <div class="lotus-corner lotus-bl">🪷</div>
    <div class="lotus-corner lotus-br">🪷</div>

    <!-- Floating hearts & petals (generated by script below) -->
    <div class="hearts-bg" id="heartsBg"></div>

    <!-- Main poem container -->
    <div class="container">
      <div class="envelope">

        <div class="title">
          <h1>💝 {POEM_TITLE} 💝</h1>
          <p class="subtitle">{POEM_SUBTITLE}</p>
        </div>

        <div class="divider">✦ ❀ ✦</div>

        {stanzas_html}

        <div class="footer">
          <p>{FOOTER_MESSAGE.replace('❤️', '')} <span class="glowing-heart">❤️</span></p>
        </div>

      </div>
    </div>

    <!-- Floating hearts & petals generator -->
    <script>
    (function() {{
      var bg = document.getElementById('heartsBg');
      var hearts = ['💕', '❤️', '💖', '💗', '🌸', '🌺'];
      // Create 22 floating hearts
      for (var i = 0; i < 22; i++) {{
        var span = document.createElement('span');
        span.className = 'heart';
        span.textContent = hearts[i % hearts.length];
        span.style.left = (Math.random() * 100).toFixed(1) + '%';
        span.style.animationDuration = (8 + Math.random() * 10).toFixed(1) + 's';
        span.style.animationDelay = (Math.random() * 14).toFixed(1) + 's';
        span.style.fontSize = (1 + Math.random() * 1.2).toFixed(2) + 'rem';
        bg.appendChild(span);
      }}
      // Create 15 petals
      for (var j = 0; j < 15; j++) {{
        var petal = document.createElement('div');
        petal.className = 'petal';
        petal.style.left = (Math.random() * 100).toFixed(1) + '%';
        petal.style.animationDuration = (10 + Math.random() * 12).toFixed(1) + 's';
        petal.style.animationDelay = (Math.random() * 16).toFixed(1) + 's';
        bg.appendChild(petal);
      }}
    }})();
    </script>

    </body>
    </html>
    """)
    return html


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
