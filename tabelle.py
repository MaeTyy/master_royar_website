import os
import matplotlib.pyplot as plt
from matplotlib.table import Table
import matplotlib as mpl
from matplotlib.font_manager import FontProperties

# 1. Liberation Sans als Ersatz für Arial
liberation_font = FontProperties(family='Liberation Sans')

# 2. Tabellenstruktur
columns = [
    "System",
    "Lokale Lauffähigkeit",
    "Open Source",
    "Anpassbarkeit",
    "Alt-DB-Kompatibilität",
    "Performanz"
]

rows = [
    ["Vanna.AI", "Je nach verwendetem LLM", "Ja – MIT-Lizenz", "Umfangreich\n– RAG plus Indexierung", "Integriert\n– Metadaten und Glossar", "Je nach Modell,\nVanna.AI selbst leichtgewichtig"],
    ["Chat2DB", "Ja mit reduziertem\nFunktionsumfang und\nje nach verwendetem LLM", "Communityversion\n– Apache 2.0", "Hauptsächlich durch\ndie Wahl des LLMs", "Problematisch bei\nnicht sprechenden Schemata", "Je nach Modell,\nChat2DB selbst ist leichtgewichtig"],
    ["Dataherald AI", "Docker läuft lokal,\njedoch je nach verwendetem LLM", "Ja – Apache 2.0", "Hoch\n– unter anderem durch Agenten und Beispiele", "Hoch\n– umfangreiche Kontextwerkzeuge", "Hoher Setup-Aufwand"],
    ["WrenAI", "Je nach verwendetem LLM", "Ja – AGPL-3.0", "Global Instructions,\nMDL, semantische Indexierung", "Mit Kontext zuverlässig", "Je nach Modell"],
    ["NSQL", "Vollständig\nlokal möglich", "Ja – Apache 2.0", "Nur über Finetuning\nvorgesehen", "Ohne Agenten schwierig,\nmit eigener Lösung möglich", "Leichtgewichtige Modelle\nvorhanden"],
    ["GPT-4", "Nein", "Nein – Proprietär", "Prompt sehr flexibel", "Gut\n– extrem umfangreiche Prompts möglich", "Nicht lokal nutzbar"],
    ["Text2SQL.ai", "Nein", "Nein – Proprietär", "Nicht anpassbar", "Keine Schemahilfe", "Nicht lokal nutzbar"],
    ["CodeS", "Vollständig lokal", "Ja – Apache 2.0", "Augmentiert und\nanpassbar", "Sehr robust", "Leichtgewichtiges Modell"],
    ["SQLCoder", "Vollständig\nlokal möglich", "Ja – Apache und CC", "Finetuning möglich", "Codebasiertes Vortraining\nund Beam Search", "Leichtgewichtiges Modell\nvorhanden"],
    ["PremSQL", "Vollständig lokal", "Ja – aber keine Lizenz\nangegeben", "Iteratives Lernen", "Execution-guided Decoding", "Prem-1B extrem schnell"],
    ["DataGPT-SQL-7B", "Lokal angekündigt", "Offen angekündigt", "DPO-Ansatz angekündigt", "Schema-Linking\nstark angekündigt", "Kein Modell veröffentlicht"]
]

# 3. Farbcodes pro Zelle
color_map = {
    "green": "#c6efce",
    "yellow": "#ffeb9c",
    "red": "#ffc7ce",
    "white": "white"
}
cell_colors = [
    ["white", "yellow", "green", "green", "green", "yellow"],
    ["white", "yellow", "green", "yellow", "yellow", "green"],
    ["white", "yellow", "green", "green", "green", "yellow"],
    ["white", "yellow", "green", "green", "green", "yellow"],
    ["white", "green",  "green", "yellow", "yellow", "green"],
    ["white", "red",    "red",   "green",  "green",  "red"],
    ["white", "red",    "red",   "red",    "red",    "red"],
    ["white", "green",  "green", "yellow", "green",  "green"],
    ["white", "green",  "green", "yellow", "green",  "green"],
    ["white", "green",  "green", "green",  "green",  "green"],
    ["white", "yellow", "yellow","yellow", "yellow", "red"]
]

# 4. Plot vorbereiten
fig, ax = plt.subplots(figsize=(16.5, 8.3))
ax.axis('off')
table = Table(ax, bbox=[0, 0, 1, 1])

n_rows, n_cols = len(rows), len(columns)
col_widths = [1.8, 3.2, 2.8, 3.2, 3.3, 2.8]
row_height = 1 / (n_rows + 1.5)

# 5. Header-Zeile
for col in range(n_cols):
    cell = table.add_cell(
        0, col,
        width=col_widths[col] / sum(col_widths),
        height=row_height,
        text=columns[col],
        loc='center',
        facecolor='lightgrey'
    )
    cell.get_text().set_fontsize(15)
    cell.get_text().set_fontproperties(liberation_font)
    cell.get_text().set_weight('bold')
    cell.get_text().set_va('center')

# 6. Inhalt
for row in range(n_rows):
    for col in range(n_cols):
        bg = color_map[cell_colors[row][col]]
        cell = table.add_cell(
            row+1, col,
            width=col_widths[col] / sum(col_widths),
            height=row_height,
            text=rows[row][col],
            loc='center',
            facecolor=bg
        )
        cell.get_text().set_fontproperties(liberation_font)
        if col == 0:
            cell.get_text().set_fontsize(14)
            cell.get_text().set_weight('bold')
        else:
            cell.get_text().set_fontsize(13)
        cell.get_text().set_va('center')

ax.add_table(table)

# 7. Speichern
os.makedirs("images", exist_ok=True)
plt.savefig("images/Vergleich.png", dpi=300, bbox_inches='tight')
plt.close()
