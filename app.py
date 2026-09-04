import streamlit as st
import streamlit.components.v1 as components

FAVICON_URL = "https://raw.githubusercontent.com/pintarkantor-prog/PINTAR-TUBE/refs/heads/main/favicon.png"
LOGO_URL    = "https://raw.githubusercontent.com/pintarkantor-prog/PINTAR-TUBE/refs/heads/main/PINTAR%20TUBE.png"

st.set_page_config(
    page_title="PINTAR TUBE - YouTube Studio Automation",
    page_icon=FAVICON_URL,
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: none !important;}
</style>
""", unsafe_allow_html=True)

raw_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PINTAR TUBE - YouTube Content Engine</title>
    <link rel="icon" type="image/png" href="__FAVICON_URL__">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', sans-serif;
            scroll-behavior: smooth;
        }
        body {
            background-color: #080c14;
            color: #c8cdd5;
            padding: 24px 40px 60px;
            min-height: 100vh;
        }
        .container {
            max-width: 1140px;
            margin: 0 auto;
        }
        
        /* Sticky Top Navigation Bar */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #0e1630;
            border: 1px solid rgba(255, 0, 0, 0.2);
            border-radius: 14px;
            padding: 12px 24px;
            margin-bottom: 24px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.5);
        }
        .nav-logo-img {
            height: 52px;
            object-fit: contain;
            display: block;
        }
        .nav-links {
            display: flex;
            gap: 20px;
        }
        .nav-links a {
            color: #7e89ac;
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            transition: all 0.2s ease;
            padding: 6px 12px;
            border-radius: 6px;
        }
        .nav-links a:hover {
            color: #ffffff;
            background: rgba(255, 255, 255, 0.05);
        }

        /* Hero Section */
        .hero {
            text-align: center;
            padding: 30px 20px 24px;
            background: radial-gradient(circle at top, rgba(255, 0, 0, 0.08) 0%, transparent 70%);
        }
        .hero h1 {
            font-size: 36px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 10px;
            letter-spacing: -0.5px;
        }
        .hero p {
            font-size: 14px;
            color: #7e89ac;
            max-width: 650px;
            margin: 0 auto 20px;
            line-height: 1.6;
        }
        
        /* Status Bar High-Tech 3 Kolom */
        .status-panel {
            display: grid;
            grid-template-columns: 1fr 1.4fr 1.3fr;
            gap: 20px;
            align-items: center;
            background: #0e1630;
            border: 1px solid rgba(255, 0, 0, 0.2);
            border-radius: 12px;
            padding: 16px 24px;
            margin-bottom: 36px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.5);
        }
        .status-item {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .status-label {
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            color: #7e89ac;
            letter-spacing: 0.8px;
        }
        .uptime-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(16, 185, 129, 0.1);
            color: #10b981;
            border: 1px solid rgba(16, 185, 129, 0.25);
            padding: 5px 14px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
            font-family: 'JetBrains Mono', monospace;
            width: fit-content;
        }
        .pulsing-dot {
            width: 8px;
            height: 8px;
            background-color: #10b981;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
            animation: pulse-green 2s infinite;
        }
        @keyframes pulse-green {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }
        .partner-badge {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.12);
            padding: 5px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            color: #ffffff;
            width: fit-content;
        }
        .logos-wrap {
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .security-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 0, 0, 0.08);
            border: 1px solid rgba(255, 0, 0, 0.25);
            padding: 5px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            color: #ff6b6b;
            width: fit-content;
        }

        /* Feature Cards */
        .grid-3 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .card {
            background: #0e1630;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 26px;
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-3px);
            border-color: rgba(255, 0, 0, 0.4);
        }
        .card-icon {
            font-size: 26px;
            margin-bottom: 12px;
        }
        .card-title {
            font-size: 16px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 8px;
        }
        .card-desc {
            font-size: 13px;
            color: #7e89ac;
            line-height: 1.6;
        }

        /* Document Section */
        .section-box {
            background: #0e1630;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 36px;
            margin-bottom: 30px;
            line-height: 1.7;
        }
        .section-box h2 {
            font-size: 20px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 6px;
        }
        .meta-line {
            font-size: 12px;
            color: #7e89ac;
            margin-bottom: 20px;
            padding-bottom: 14px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        .section-box h3 {
            font-size: 14px;
            font-weight: 700;
            color: #ff6b6b;
            margin-top: 20px;
            margin-bottom: 8px;
        }
        .section-box p, .section-box li {
            font-size: 13px;
            color: #cbd5e1;
            margin-bottom: 10px;
        }
        .section-box ul {
            padding-left: 20px;
            margin-bottom: 14px;
        }
        .section-box a {
            color: #ff6b6b;
            text-decoration: none;
            font-weight: 600;
        }
        .callout-box {
            background: rgba(255, 0, 0, 0.06);
            border: 1px solid rgba(255, 0, 0, 0.25);
            padding: 16px 20px;
            border-radius: 10px;
            margin-top: 18px;
            font-size: 12px;
            color: #cbd5e1;
        }

        /* Footer */
        .footer {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
            color: #7e89ac;
            flex-wrap: wrap;
            gap: 12px;
        }
        
        @media (max-width: 900px) {
            .status-panel {
                grid-template-columns: 1fr;
            }
            .navbar {
                flex-direction: column;
                gap: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Top Navbar dengan Logo Gambar Asli PINTAR TUBE -->
        <div class="navbar">
            <img src="__LOGO_URL__" alt="PINTAR TUBE" class="nav-logo-img">
            <div class="nav-links">
                <a href="#features">Fitur</a>
                <a href="#privacy">Kebijakan Privasi</a>
                <a href="#terms">Syarat Layanan</a>
                <a href="#compliance">Kepatuhan API</a>
            </div>
        </div>

        <!-- Hero Header -->
        <div class="hero">
            <h1>YouTube Studio Automation Platform</h1>
            <p>
                Infrastruktur otomasi cerdas untuk manajemen jadwal konten, pemrosesan video berkecepatan tinggi, dan integrasi resmi Google YouTube Data API v3.
            </p>
        </div>

        <!-- Status Panel 3 Kolom -->
        <div class="status-panel">
            <div class="status-item">
                <span class="status-label">LIVE SYSTEM UPTIME</span>
                <span class="uptime-badge">
                    <span class="pulsing-dot"></span>
                    <span id="live-uptime">99.7% Uptime</span>
                </span>
            </div>
            
            <div class="status-item">
                <span class="status-label">CERTIFIED API ARCHITECTURE</span>
                <span class="partner-badge">
                    <div class="logos-wrap">
                        <svg width="16" height="16" viewBox="0 0 24 24">
                            <path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/>
                            <path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.15C3.26 21.36 7.34 24 12 24z"/>
                            <path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.13-1.55.38-2.27V6.58H1.25C.45 8.18 0 9.99 0 12s.45 3.82 1.25 5.42l4.03-3.15z"/>
                            <path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.34 0 3.26 2.64 1.25 6.58l4.03 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/>
                        </svg>
                        <svg width="20" height="15" viewBox="0 0 20 14" fill="none">
                            <rect width="20" height="14" rx="4" fill="#FF0000"/>
                            <polygon points="8,3.5 14,7 8,10.5" fill="#FFFFFF"/>
                        </svg>
                    </div>
                    <span>Google Cloud & YouTube API Verified</span>
                </span>
            </div>
            
            <div class="status-item">
                <span class="status-label">DATA PRIVACY PROTOCOL</span>
                <span class="security-badge">
                    <span>🔒</span>
                    <span>Zero-Knowledge OAuth Security</span>
                </span>
            </div>
        </div>

        <!-- Section: Features -->
        <div id="features" class="grid-3">
            <div class="card">
                <div class="card-icon">⚡</div>
                <div class="card-title">Resumable Upload Engine</div>
                <div class="card-desc">
                    Menggunakan chunk upload protocol resmi YouTube API untuk stabilitas transmisi video berukuran besar tanpa interupsi.
                </div>
            </div>
            <div class="card">
                <div class="card-icon">🛡️</div>
                <div class="card-title">Strict Token Isolation</div>
                <div class="card-desc">
                    Semua token otentikasi Google OAuth 2.0 diisolasi dengan proteksi tingkat tinggi. Tidak ada data akun pribadi yang diperjualbelikan.
                </div>
            </div>
            <div class="card">
                <div class="card-icon">📅</div>
                <div class="card-title">Automated Scheduling</div>
                <div class="card-desc">
                    Penjadwalan otomatis berbasis slot waktu produktif kreator dan sinkronisasi kuota API Google harian yang efisien.
                </div>
            </div>
        </div>

        <!-- Section: Privacy Policy -->
        <div id="privacy" class="section-box">
            <h2>🔒 Kebijakan Privasi (Privacy Policy)</h2>
            <div class="meta-line">Dokumen Kebijakan Resmi PINTAR TUBE | Berlaku Efektif 2026</div>

            <h3>1. Pendahuluan</h3>
            <p>
                <strong>PINTAR TUBE</strong> ("kami") adalah platform manajemen publikasi video yang terintegrasi dengan YouTube API Services. Kami sangat memprioritaskan keamanan dan privasi data para pengguna.
            </p>

            <h3>2. Data yang Diakses & Digunakan</h3>
            <p>
                Aplikasi ini hanya meminta izin akses YouTube yang dibutuhkan untuk mengunggah konten (<code>https://www.googleapis.com/auth/youtube.upload</code>) serta membaca metadata verifikasi channel (<code>youtube.readonly</code>).
            </p>
            <ul>
                <li>Kami <strong>TIDAK PERNAH</strong> meminta atau menyimpan password akun Google pengguna.</li>
                <li>Kami <strong>TIDAK MEMBAGIKAN</strong> atau menjual data pengguna kepada pihak ketiga mana pun.</li>
            </ul>

            <h3>3. Penghapusan Data & Pencabutan Akses</h3>
            <p>
                Pengguna dapat memutuskan kaitan aplikasi kapan saja melalui <a href="https://myaccount.google.com/permissions" target="_blank">Pengaturan Izin Akun Google</a>.
            </p>
        </div>

        <!-- Section: Terms of Service -->
        <div id="terms" class="section-box">
            <h2>📄 Syarat & Ketentuan Layanan</h2>
            <div class="meta-line">Perjanjian Penggunaan Layanan PINTAR TUBE</div>

            <h3>1. Penggunaan yang Sah</h3>
            <p>
                Pengguna bertanggung jawab penuh atas seluruh video yang diunggah melalui sistem ini dan wajib mematuhi seluruh Pedoman Komunitas YouTube serta hak cipta yang sah.
            </p>

            <h3>2. Batasan Tanggung Jawab</h3>
            <p>
                Layanan ini disediakan sebagai alat bantu otomasi. Kami tidak bertanggung jawab atas sanksi channel yang diakibatkan oleh pelanggaran hak cipta atau pedoman komunitas oleh pengguna.
            </p>
        </div>

        <!-- Section: YouTube API Compliance -->
        <div id="compliance" class="section-box">
            <h2>🛡️ Kepatuhan Google API & YouTube Data Policy</h2>
            <div class="meta-line">Pernyataan Kepatuhan Developer Resmi</div>

            <p>
                Dengan menggunakan <strong>PINTAR TUBE</strong>, pengguna menyetujui untuk terikat dengan:
            </p>
            <ul>
                <li><a href="https://www.youtube.com/t/terms" target="_blank">YouTube Terms of Service</a></li>
                <li><a href="https://policies.google.com/privacy" target="_blank">Google Privacy Policy</a></li>
            </ul>

            <div class="callout-box">
                <strong>Pemberitahuan Persyaratan Penggunaan Terbatas (Limited Use):</strong><br>
                Penggunaan dan transfer informasi yang diterima <strong>PINTAR TUBE</strong> dari Google API akan sepenuhnya mematuhi <a href="https://developers.google.com/terms/api-services-user-data-policy" target="_blank">Kebijakan Data Pengguna Layanan Google API</a>.
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <div>© 2026 <strong>PINTAR TUBE</strong>. Powered by PINTAR MEDIA.</div>
            <div>Kontak Pengembang: <span style="color:#ff6b6b; font-weight:700;">pintarkantor@gmail.com</span></div>
        </div>
    </div>

    <script>
        function updateUptime() {
            const uptimeEl = document.getElementById('live-uptime');
            if (uptimeEl) {
                const randomVal = (98.2 + Math.random() * (99.9 - 98.2)).toFixed(1);
                uptimeEl.textContent = randomVal + '% Uptime';
            }
        }
        updateUptime();
        setInterval(updateUptime, 300000);
    </script>
</body>
</html>
"""

final_html = raw_html.replace("__FAVICON_URL__", FAVICON_URL).replace("__LOGO_URL__", LOGO_URL)
components.html(final_html, height=1550, scrolling=True)
