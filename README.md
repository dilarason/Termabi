# Termabi 🧠💻

**Termabi**, terminalde doğal dil ile konuşabilen bir yapay zekâ asistanıdır. Kod yazmak, komutları çalıştırmak, sistem hatalarını yorumlamak gibi işlemleri doğal Türkçe ile yapmanı sağlar.

## 🚀 Başlangıç

### Kurulum

```bash
git clone https://github.com/dilarason/termabi.git
cd termabi
pip install -r requirements.txt
```

### API Anahtarını Ayarlama

```bash
mkdir -p ~/.termabi
echo 'api_key: "YOUR_OPENAI_API_KEY"' > ~/.termabi/config.yaml
```

### Kullanım

```bash
python termabi.py komut "bu klasördeki zip dosyalarını sil"
```

Abi modunu aktif etmek için:

```bash
python termabi.py komut "neden sistem servisi çöküyor" --abi-mode
```

## 📁 Dosya Yapısı

- `termabi.py`: Ana uygulama dosyası
- `prompts/`: Prompt şablonları
- `requirements.txt`: Gerekli Python modülleri
- `LICENSE`: Açık kaynak lisansı (MIT)

## 📧 İletişim

Proje Sahibi: [dilarason@termabi.com](mailto:dilarason@termabi.com)

## 🪪 Lisans

MIT License
