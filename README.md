# KaelAgent

🚀 **GPT-4 Tabanlı Terminal Ajanı – Flutter Geliştiricileri İçin**

KaelAgent, Flutter projelerinde hata tespiti, debug analizi ve opsiyonel düzeltme işlemlerini yapabilen otonom bir terminal tabanlı ajan sistemidir. GPT-4 destekli bu yapı, geliştiricilerin CLI üzerinden hızlıca geri bildirim almasını sağlar.

---

## 🧠 Özellikler

- Flutter projelerinde derleme ve çalışma zamanı hatalarını tanımlar
- İsteğe bağlı olarak hata düzeltmeleri önerir ya da doğrudan yapar *(fail-safe modu desteklenir)*
- Geliştiriciye sadece bilgi vermekle kalmaz, aynı zamanda aksiyon alır
- Basit komutlarla terminalden çalıştırılır
- Dosya içeriğini bozmadan sadece gerekli yerleri düzenlemeyi hedefler

---

## 🔧 Kullanım Durumu (Başlangıç Aşaması)

> Bu proje hâlâ deneyseldir ve **sadece kişisel kullanım** içindir. Kodlar henüz tam anlamıyla yayımlanmamıştır.

- `kael_agent.py` (veya `main.py`) dosyasını çalıştırarak CLI üzerinden terminal içi kontrol başlatılır
- Hedef proje dizini belirtildikten sonra `flutter pub get`, `flutter run`, `flutter doctor` çıktıları analiz edilir
- Algılanan hatalar için kullanıcıya düzeltme önerilir

---

## 📦 Kurulum (yakında)

```
git clone https://github.com/sudofurkanbey/KaelAgent.git
cd KaelAgent
python kael_agent.py
```

---

## 📁 Planlanan Yapı

```
KaelAgent/
├── kael_agent.py            # Ana ajan betiği
├── modules/
│   ├── analyzer.py          # Hata analiz motoru
│   ├── fixer.py             # Otomatik düzeltici modül
│   └── reporter.py          # Sonuç raporu oluşturucu
├── configs/
│   └── settings.json        # Ajan konfigürasyon ayarları
├── .gitignore
└── README.md
```

---

## ⚠️ Uyarı

- Ajan, gerçek projelere uygulanmadan önce izole test dizinlerinde denenmelidir.
- Geliştirme hâlindedir. Kodlar paylaşıldıkça `Issues` ve `Pull Request` kısmı aktif hale gelecektir.

---

## ✍️ Katkı ve Lisans

> Proje şu an **özel** ve katkıya kapalıdır. Daha sonra açık hale geldiğinde lisans bilgisi eklenecektir.

---

🧬 **Kodla, boz, düzelt, öğren. KaelAgent her zaman yanında.**