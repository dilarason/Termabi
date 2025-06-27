
import json
import typer
from rich import print
from rich.prompt import Prompt, Confirm
import subprocess
import os

app = typer.Typer()

# JSON komut veri tabanını yükle
def load_commands():
    path = os.path.join(os.path.dirname(__file__), "data/commands.json")
    if not os.path.exists(path):
        print("[bold red]Komut veritabanı bulunamadı: data/commands.json[/bold red]")
        raise FileNotFoundError("Komut veritabanı eksik")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.command()
def komut(yaz: str):
    '''
    Doğal dil girdisini bash komutuna çevirir ve çalıştırmak ister misin diye sorar.
    '''
    commands = load_commands()
    eslesen = None

    for item in commands:
        if yaz.strip().lower() in item["input"]:
            eslesen = item
            break

    if not eslesen:
        print("[bold yellow]❓ Bu komutu anlayamadım. Komut veri tabanına eklenmemiş olabilir.[/bold yellow]")
        raise typer.Exit()

    print(f"[bold blue]💬 Eşleşen komut:[/bold blue] {eslesen['bash']}")
    print(f"🧠 Açıklama: {eslesen['description']}\n")

    if Confirm.ask("Komutu terminalde çalıştırmak ister misin?"):
        try:
            result = subprocess.run(eslesen["bash"], shell=True, check=True, capture_output=True, text=True)
            print(f"[green]✅ Başarılı çıktı:[/green]\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"[red]❌ Hata:[/red]\n{e.stderr}")
    else:
        print("[bold yellow]Komut çalıştırılmadı.[/bold yellow]")

if __name__ == "__main__":
    app()
