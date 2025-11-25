import os
import matplotlib.pyplot as plt
from pathlib import Path

# Ruta robusta
OUTPUT_DIR = Path(__file__).parent.parent / "files" / "output"

try:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
except Exception as e:
    print(f"Error creando directorio: {e}")
    exit(1)

output_path = OUTPUT_DIR / "stocks.png"

# Opción 1: Crear siempre (sobrescribe si existe)
try:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot([1, 2, 3], [10, 15, 13], marker='o', linewidth=2)
    ax.set_title("Stock Price Over Time", fontsize=14)
    ax.set_xlabel("Day")
    ax.set_ylabel("Price ($)")
    ax.grid(True, alpha=0.3)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"✓ Gráfico guardado en: {output_path}")
except Exception as e:
    print(f"✗ Error creando gráfico: {e}")
finally:
    plt.close(fig)

# Opción 2: Crear solo si no existe (tu lógica original mejorada)
"""
if not output_path.exists():
    try:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot([1, 2, 3], [10, 15, 13], marker='o')
        ax.set_title("Stock Price")
        ax.set_xlabel("Day")
        ax.set_ylabel("Price ($)")
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        print(f"✓ Creado: {output_path}")
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        plt.close(fig)
else:
    print(f"⚠ Ya existe: {output_path}")
"""