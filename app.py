import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="NOVEL-WEBdesigns", page_icon="🚀", layout="wide")

# 2. Elite 2026 Agency CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.88), rgba(0, 0, 0, 0.88)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072');
        background-attachment: fixed;
        background-size: cover;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    .sticky-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: #1e40af;
        color: #ffffff;
        text-align: center;
        padding: 12px;
        z-index: 9999;
        font-weight: 700;
        border-bottom: 2px solid #3b82f6;
    }

    .glass-card {
        background: rgba(15, 23, 42, 0.8);
        backdrop-filter: blur(12px);
        padding: 35px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 30px;
    }

    .service-tag {
        display: inline-block;
        background: rgba(59, 130, 246, 0.2);
        color: #3b82f6;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        margin-bottom: 10px;
        border: 1px solid #3b82f6;
    }

    .metric-box {
        text-align: center;
        padding: 25px;
        background: rgba(59, 130, 246, 0.1);
        border-radius: 15px;
        border: 1px solid #3b82f6;
    }
    
    .footer {
        padding: 60px 0;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        background: rgba(10, 10, 10, 0.5);
    }

    .spacer { padding: 60px 0; }
    h1, h2, h3 { color: #ffffff !important; }
    </style>
    
    <div class="sticky-bar">
        📞 WhatsApp: +91 7075172518 | 📧 Email: sanjanareddy2607@gmail.com
    </div>
    """, unsafe_allow_html=True) # FIXED: unsafe_allow_html

# --- SECTION 1: HERO ---
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
col_h1, col_h2 = st.columns([1.2, 1])
with col_h1:
    st.markdown("""
        <h1 style='font-size: 4rem; line-height: 1.1;'>ELITE Website <br><span style='color:#3b82f6;'>development</span></h1>
        <p style='font-size: 1.3rem; margin-top: 20px;'>I specialize in building high-conversion,  websites that turn visitors into loyal clients within 24 hours.</p>
    """, unsafe_allow_html=True)
    

with col_h2:
    st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=2072", use_container_width=True)

# --- SECTION 2: SPECIALIZED SERVICES (NEW) ---
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>What I Build for You</h2>", unsafe_allow_html=True)
s1, s2, s3 = st.columns(3)
with s1:
    st.markdown("""<div class="glass-card">
        <div class="service-tag">High Conversion</div>
        <h3>Landing Pages</h3>
        <p>Perfect for Facebook/Google Ads. Designed to capture leads instantly with integrated WhatsApp hooks.</p>
    </div>""", unsafe_allow_html=True)
with s2:
    st.markdown("""<div class="glass-card">
        <div class="service-tag">AI-Powered</div>
        <h3>Custom Dashboards</h3>
        <p>Interactive data visualizations and management tools for small businesses and startups.</p>
    </div>""", unsafe_allow_html=True)
with s3:
    st.markdown("""<div class="glass-card">
        <div class="service-tag">0 Monthly Fees</div>
        <h3>Corporate Portfolios</h3>
        <p>A "Digital Empire" for consultants and experts to showcase authority and book high-ticket clients.</p>
    </div>""", unsafe_allow_html=True)

# --- SECTION 3: CLIENT PERSONAS (WHO I HELP) ---
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
col_p1, col_p2 = st.columns([1, 1.5])
with col_p1:
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070", use_container_width=True)
with col_p2:
    st.markdown("""
        <h2>Who Can Benefit?</h2>
        <div class="glass-card">
            <h4>1. Independent Consultants & Coaches</h4>
            <p>Showcase your expertise with a site that looks like a million-dollar brand.</p>
            <h4>2. Tech Startups</h4>
            <p>Get your MVP (Minimum Viable Product) or landing page live in 24 hours to start testing the market.</p>
            <h4>3. Small Business Owners</h4>
            <p>Move away from expensive monthly website builders. Own your code, own your platform, pay ₹0 in monthly fees.</p>
        </div>
    """, unsafe_allow_html=True)

# --- SECTION 4: PERFORMANCE DASHBOARD ---
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>Agency Performance Metrics</h2>", unsafe_allow_html=True)
db1, db2, db3, db4 = st.columns(4)
with db1:
    st.markdown('<div class="metric-box"><div class="metric-value">24h</div><div>Uptime Delivery</div></div>', unsafe_allow_html=True)
with db2:
    st.markdown('<div class="metric-box"><div class="metric-value">100%</div><div>Mobile Response</div></div>', unsafe_allow_html=True)
with db3:
    st.markdown('<div class="metric-box"><div class="metric-value">0</div><div>Recurring Costs</div></div>', unsafe_allow_html=True)
with db4:
    st.markdown('<div class="metric-box"><div class="metric-value">5★</div><div>Client Success</div></div>', unsafe_allow_html=True)

# --- SECTION 5: TESTIMONIALS ---
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
t1, t2, t3 = st.columns(3)
with t1:
    st.markdown('<div class="glass-card"><i>"Sanjana delivered a premium site overnight. Phenomenal speed and quality."</i><br><br><b>- Rajesh K.</b></div>', unsafe_allow_html=True)
with t2:
    st.markdown('<div class="glass-card"><i>"The professional dashboard and WhatsApp integration are game changers."</i><br><br><b>- Anita M.</b></div>', unsafe_allow_html=True)
with t3:
    st.markdown('<div class="glass-card"><i>"Clean design, zero hidden costs. Exactly what my startup needed."</i><br><br><b>- Vikram S.</b></div>', unsafe_allow_html=True)

# --- SECTION 6: CALL TO ACTION ---
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
wa_num = "917075172518" # Replace with your REAL number
wa_url = f"https://wa.me/{wa_num}?text=Hi%20Sanjana,%20I'm%20ready%20to%20start%20my%20Digital%20Empire!"
st.markdown(f"""
    <div style='text-align:center;'>
        <a href="{wa_url}" target="_blank" style="text-decoration:none;">
            <button style="background-color:#10b981; color:white; padding:25px 80px; border:none; border-radius:15px; font-size:1.8rem; font-weight:800; cursor:pointer; box-shadow: 0 10px 30px rgba(16,185,129,0.3);">
                💬 Contact Me on WhatsApp
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# --- SECTION 7: FOOTER ---
st.markdown(f"""
    <div class="footer">
        <p style="font-size:1.3rem; color:#ffffff;"><b>Sanjana Digital Solutions</b></p>
        <p>Expert Web Development | 📧 sanjanareddy2607@gmail.com | 📞 +91 7075172518</p>
        <p>© 2026 Sanjana NOVEL-WEBdesigns. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)