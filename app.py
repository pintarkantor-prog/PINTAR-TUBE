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
            background-color: #090d16;
            color: #c8cdd5;
            padding: 24px 40px 60px;
            min-height: 100vh;
        }
        .container {
            max-width: 1140px;
            margin: 0 auto;
        }
        
        /* Top Navbar Terintegrasi dengan Status Live & Verified */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #0e1630;
            border: 1px solid rgba(129, 140, 248, 0.15);
            border-radius: 14px;
            padding: 14px 24px;
            margin-bottom: 30px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.5);
            position: relative;
            overflow: hidden;
        }
        .navbar::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, #6c72ff, #10b981, transparent);
            animation: scanline 4s linear infinite;
        }
        @keyframes scanline {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }

        .nav-logo-img {
            height: 52px;
            object-fit: contain;
            display: block;
        }
        .nav-status-wrap {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }
        
        /* Badges */
        .uptime-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(16, 185, 129, 0.1);
            color: #10b981;
            border: 1px solid rgba(16, 185, 129, 0.25);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            font-family: 'JetBrains Mono', monospace;
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
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            color: #ffffff;
            transition: all 0.2s ease;
        }
        .partner-badge:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(129, 140, 248, 0.4);
        }
        .logos-wrap {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* Feature Cards */
        .grid-3 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 26px;
        }
        .card {
            background: #0e1630;
            border: 1px solid rgba(129, 140, 248, 0.12);
            border-radius: 14px;
            padding: 26px;
            transition: all 0.2s ease;
        }
        .card:hover {
            transform: translateY(-2px);
            border-color: rgba(129, 140, 248, 0.4);
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
            border: 1px solid rgba(129, 140, 248, 0.15);
            border-radius: 14px;
            padding: 34px;
            margin-bottom: 24px;
            line-height: 1.7;
        }
        .section-box h2 {
            font-size: 19px;
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
            color: #818cf8;
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
            color: #818cf8;
            text-decoration: none;
            font-weight: 600;
        }
        .section-box a:hover {
            text-decoration: underline;
        }
        .callout-box {
            background: rgba(108, 114, 255, 0.08);
            border: 1px solid rgba(108, 114, 255, 0.25);
            padding: 16px 20px;
            border-radius: 10px;
            margin-top: 18px;
            font-size: 12px;
            color: #cbd5e1;
        }

        /* Footer */
        .footer {
            margin-top: 36px;
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
            .navbar {
                flex-direction: column;
                gap: 16px;
                align-items: flex-start;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Top Navbar dengan Logo PINTAR TUBE di Kiri & Status di Kanan -->
        <div class="navbar">
            <img src="__LOGO_URL__" alt="PINTAR TUBE" class="nav-logo-img">
            
            <div class="nav-status-wrap">
                <!-- Live Uptime -->
                <span class="uptime-badge">
                    <span class="pulsing-dot"></span>
                    <span id="live-uptime">99.8% Uptime</span>
                </span>
                
                <!-- Google & YouTube Certified -->
                <span class="partner-badge">
                    <div class="logos-wrap">
                        <!-- Logo Google Asli 4 Warna -->
                        <svg width="16" height="16" viewBox="0 0 24 24">
                            <path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/>
                            <path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.15C3.26 21.36 7.34 24 12 24z"/>
                            <path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.13-1.55.38-2.27V6.58H1.25C.45 8.18 0 9.99 0 12s.
