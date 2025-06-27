# termabi.py

import typer
from rich import print
from rich.prompt import Confirm
import subprocess
import os
import logging

app = typer.Typer()

PROMPT_PATH = os.path.join(os.path.dirname(__file__), "prompts/termabi_prompt.txt")
LOG_PATH = os.path.expanduser("~/.termabi/termabi.log")

os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_prompt():
    if not os.path.exists(PROMPT_PATH):
        raise FileNotFoundError("Prompt dosyası bulunamadı.")
    with open(PROMPT_PATH, "r") as f:
        return f.read()

@app.command()
def komut(yaz: str):
    """
    Yazdığın cümleyi bash komutuna çevirip çalıştırır.
    """
    try:
        prompt = load_prompt()
        print(f"[bold green]🧠 Termabi mantık kuruyor...[/bold green]")
        print(f"[blue]Kullanıcı girdiği:[/blue] {yaz}")

        # Şimdilik sahte öneri (API yok)
        bash_komutu = f"echo '{yaz}' komutu henüz AI tarafından çevrilmedi."

        print(f"[bold blue]🛠️ Termabi önerisi:[/bold blue] {bash_komutu}")

        if Confirm.ask("Bu komutu çalıştırmak istiyor musun?"):
            result = subprocess.run(bash_komutu, shell=True, check=True, capture_output=True, text=True)
            print(f"[green]✅ Komut sonucu:[/green]\n{result.stdout}")
            logging.info(f"Komut: {bash_komutu}\nÇıktı: {result.stdout}")
        else:
            print("[yellow]🚫 Komut iptal edildi.[/yellow]")

    except Exception as e:
        print(f"[red]Hata oluştu:[/red] {e}")
        logging.exception("Beklenmeyen hata")

if __name__ == "__main__":
    app()
