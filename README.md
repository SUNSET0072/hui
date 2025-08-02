<!DOCTYPE html>
<html lang="zh-CN"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SoundWave 2025 音乐节</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.8/dist/chart.umd.min.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&amp;display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#6C2BD9', // 主色调：深紫色
                        secondary: '#00E5FF', // 辅助色：霓虹蓝
                        accent: '#FF00FF', // 强调色：霓虹粉
                        dark: '#0F172A', // 深色背景
                        light: '#F8FAFC', // 浅色文本
                    },
                    fontFamily: {
                        inter: ['Inter', 'sans-serif'],
                    },
                    animation: {
                        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                        'float': 'float 6s ease-in-out infinite',
                        'glow': 'glow 2s ease-in-out infinite alternate',
                    },
                    keyframes: {
                        float: {
                            '0%, 100%': { transform: 'translateY(0)' },
                            '50%': { transform: 'translateY(-10px)' },
                        },
                        glow: {
                            '0%': { boxShadow: '0 0 5px rgba(108, 43, 217, 0.5)' },
                            '100%': { boxShadow: '0 0 20px rgba(108, 43, 217, 0.8), 0 0 30px rgba(0, 229, 255, 0.6)' },
                        }
                    }
                },
            }
        }
    </script>
    
    <style type="text/tailwindcss">
        @layer utilities {
            .content-auto {
                content-visibility: auto;
            }
            .text-shadow {
                text-shadow: 0 0 8px rgba(108, 43, 217, 0.6);
            }
            .text-shadow-glow {
                text-shadow: 0 0 10px rgba(108, 43, 217, 0.8), 0 0 20px rgba(0, 229, 255, 0.6);
            }
            .backdrop-blur-xl {
                backdrop-filter: blur(20px);
            }
            .scrollbar-hide::-webkit-scrollbar {
                display: none;
            }
            .mask-gradient {
                mask-image: linear-gradient(to bottom, black 85%, transparent 100%);
                -webkit-mask-image: linear-gradient(to bottom, black 85%, transparent 100%);
            }
            .hover-scale {
                transition: transform 0.3s ease;
            }
            .hover-scale:hover {
                transform: scale(1.05);
            }
        }
    </style>
</head>
<body class="font-inter bg-dark text-light min-h-screen overflow-x-hidden">
    <!-- 导航栏 -->
    <nav id="navbar" class="fixed top-0 left-0 right-0 z-50 transition-all duration-300">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center backdrop-blur-xl bg-dark/70">
            <a href="#" class="flex items-center gap-2">
                <div class="w-10 h-10 rounded-full bg-gradient-to-r from-primary to-secondary flex items-center justify-center">
                    <i class="fa fa-music text-white"></i>
                </div>
                <span class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">SoundWave</span>
            </a>
            
            <!-- 桌面导航 -->
            <div class="hidden md:flex items-center space-x-8">
                <a href="#about" class="text-white hover:text-secondary transition-colors">关于</a>
                <a href="#schedule" class="text-white hover:text-secondary transition-colors">时间表</a>
                <a href="#artists" class="text-white hover:text-secondary transition-colors">艺人</a>
                <a href="#tickets" class="text-white hover:text-secondary transition-colors">购票</a>
                <button class="bg-gradient-to-r from-primary to-secondary px-6 py-2 rounded-full font-medium hover:opacity-90 transition-opacity">
                    立即购票
                </button>
            </div>
            
            <!-- 移动端菜单按钮 -->
            <button id="menu-toggle" class="md:hidden text-white text-2xl">
                <i class="fa fa-bars"></i>
            </button>
        </div>
        
        <!-- 移动端导航菜单 -->
        <div id="mobile-menu" class="hidden md:hidden backdrop-blur-xl bg-dark/90">
            <div class="container mx-auto px-4 py-4 flex flex-col space-y-4">
                <a href="#about" class="text-white hover:text-secondary transition-colors py-2">关于</a>
                <a href="#schedule" class="text-white hover:text-secondary transition-colors py-2">时间表</a>
                <a href="#artists" class="text-white hover:text-secondary transition-colors py-2">艺人</a>
                <a href="#tickets" class="text-white hover:text-secondary transition-colors py-2">购票</a>
                <button class="bg-gradient-to-r from-primary to-secondary px-6 py-3 rounded-full font-medium hover:opacity-90 transition-opacity">
                    立即购票
                </button>
            </div>
        </div>
    </nav>

    <!-- 英雄区域/动态海报 -->
    <section id="hero" class="relative h-screen flex items-center justify-center overflow-hidden">
        <!-- 背景动画 -->
        <div class="absolute inset-0 z-0">
            <div class="absolute inset-0 bg-gradient-to-b from-dark/80 to-dark"></div>
            <div class="absolute top-0 left-0 w-full h-full">
                <!-- 粒子效果 -->
                <div id="particles" class="absolute inset-0"></div>
            </div>
        </div>
        
        <!-- 主标题 -->
        <div class="container mx-auto px-4 z-10 text-center">
            <h1 class="text-[clamp(2.5rem,8vw,5rem)] font-extrabold mb-6 text-shadow-glow">
                <span class="block bg-clip-text text-transparent bg-gradient-to-r from-primary via-secondary to-accent">SOUNDWAVE</span>
                <span class="block text-white mt-2">2025 音乐节</span>
            </h1>
            <p class="text-[clamp(1rem,3vw,1.5rem)] text-white/80 max-w-3xl mx-auto mb-10">
                7月15-17日 · 上海世博公园 · 汇聚全球顶尖音乐人
            </p>
            
            <!-- 倒计时 -->
            <div id="countdown" class="flex justify-center gap-4 md:gap-8 mb-12">
                <div class="bg-dark/50 backdrop-blur-xl p-4 md:p-6 rounded-xl border border-white/10">
                    <div id="days" class="text-3xl md:text-5xl font-bold text-secondary">00</div>
                    <div class="text-xs md:text-sm text-white/70 mt-1">天</div>
                </div>
                <div class="bg-dark/50 backdrop-blur-xl p-4 md:p-6 rounded-xl border border-white/10">
                    <div id="hours" class="text-3xl md:text-5xl font-bold text-secondary">00</div>
                    <div class="text-xs md:text-sm text-white/70 mt-1">时</div>
                </div>
                <div class="bg-dark/50 backdrop-blur-xl p-4 md:p-6 rounded-xl border border-white/10">
                    <div id="minutes" class="text-3xl md:text-5xl font-bold text-secondary">00</div>
                    <div class="text-xs md:text-sm text-white/70 mt-1">分</div>
                </div>
                <div class="bg-dark/50 backdrop-blur-xl p-4 md:p-6 rounded-xl border border-white/10">
                    <div id="seconds" class="text-3xl md:text-5xl font-bold text-secondary">00</div>
                    <div class="text-xs md:text-sm text-white/70 mt-1">秒</div>
                </div>
            </div>
            
            <div class="flex flex-col sm:flex-row justify-center gap-4">
                <button class="bg-gradient-to-r from-primary to-secondary px-8 py-4 rounded-full font-bold text-lg hover-scale">
                    立即购票
                </button>
                <button class="bg-transparent border-2 border-white/30 hover:border-white/60 px-8 py-4 rounded-full font-bold text-lg hover-scale transition-colors">
                    查看阵容
                </button>
            </div>
        </div>
        
        <!-- 向下滚动指示 -->
        <div class="absolute bottom-10 left-1/2 transform -translate-x-1/2 animate-bounce">
            <a href="#about" class="text-white/70 hover:text-white">
                <i class="fa fa-angle-down text-3xl"></i>
            </a>
        </div>
    </section>

    <!-- 关于区域 -->
    <section id="about" class="py-24 bg-gradient-to-b from-dark to-dark/95">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto text-center mb-16">
                <h2 class="text-[clamp(1.8rem,5vw,3rem)] font-bold mb-6">
                    <span class="bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">关于音乐节</span>
                </h2>
                <p class="text-white/80 text-lg leading-relaxed">
                    SoundWave 2025 音乐节是一场为期三天的音乐盛宴，汇集了电子、摇滚、嘻哈等多种音乐风格。我们邀请了来自全球各地的顶级音乐人，为你带来震撼的现场表演。
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-dark/50 backdrop-blur-lg p-8 rounded-2xl border border-white/10 hover-scale">
                    <div class="w-16 h-16 rounded-full bg-primary/20 flex items-center justify-center mb-6">
                        <i class="fa fa-music text-2xl text-primary"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">多元音乐风格</h3>
                    <p class="text-white/70">电子、摇滚、嘻哈、民谣等多种音乐风格的完美融合，满足不同音乐爱好者的需求。</p>
                </div>
                
                <div class="bg-dark/50 backdrop-blur-lg p-8 rounded-2xl border border-white/10 hover-scale">
                    <div class="w-16 h-16 rounded-full bg-secondary/20 flex items-center justify-center mb-6">
                        <i class="fa fa-globe text-2xl text-secondary"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">国际顶尖阵容</h3>
                    <p class="text-white/70">来自全球20多个国家的50多位知名音乐人将带来精彩表演，打造无与伦比的视听盛宴。</p>
                </div>
                
                <div class="bg-dark/50 backdrop-blur-lg p-8 rounded-2xl border border-white/10 hover-scale">
                    <div class="w-16 h-16 rounded-full bg-accent/20 flex items-center justify-center mb-6">
                        <i class="fa fa-users text-2xl text-accent"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">沉浸式体验</h3>
                    <p class="text-white/70">除了精彩的音乐表演，还有艺术装置、美食区、互动体验等多种元素，打造全方位的音乐节体验。</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 演出时间表 -->
    <section id="schedule" class="py-24 bg-dark/95">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto text-center mb-16">
                <h2 class="text-[clamp(1.8rem,5vw,3rem)] font-bold mb-6">
                    <span class="bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">演出时间表</span>
                </h2>
                <p class="text-white/80 text-lg leading-relaxed">
                    三天的音乐盛宴，五大舞台，超过50场精彩演出。提前规划你的行程，不错过任何一位心仪艺人的表演。
                </p>
            </div>
            
            <!-- 日期选择器 -->
            <div class="flex justify-center mb-12">
                <div class="inline-flex p-1 bg-dark/50 rounded-full border border-white/10">
                    <button class="schedule-day-btn active px-6 py-3 rounded-full font-medium transition-all" data-day="day1">
                        7月15日
                    </button>
                    <button class="schedule-day-btn px-6 py-3 rounded-full font-medium transition-all" data-day="day2">
                        7月16日
                    </button>
                    <button class="schedule-day-btn px-6 py-3 rounded-full font-medium transition-all" data-day="day3">
                        7月17日
                    </button>
                </div>
            </div>
            
            <!-- 时间表内容 -->
            <div class="schedule-content">
                <!-- 第一天 -->
                <div id="day1" class="schedule-day block">
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                        <!-- 主舞台 -->
                        <div class="bg-dark/50 backdrop-blur-lg p-8 rounded-2xl border border-white/10">
                            <h3 class="text-xl font-bold mb-6 flex items-center">
                                <span class="w-3 h-3 rounded-full bg-primary mr-2"></span>
                                主舞台
                            </h3>
                            <div class="space-y-6">
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">16:00</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Electric Pulse</h4>
                                        <p class="text-white/70 text-sm">电子音乐</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">18:30</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Cosmic Waves</h4>
                                        <p class="text-white/70 text-sm">迷幻摇滚</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">21:00</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Neon Horizon</h4>
                                        <p class="text-white/70 text-sm">电子流行</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 电子舞台 -->
                        <div class="bg-dark/50 backdrop-blur-lg p-8 rounded-2xl border border-white/10">
                            <h3 class="text-xl font-bold mb-6 flex items-center">
                                <span class="w-3 h-3 rounded-full bg-secondary mr-2"></span>
                                电子舞台
                            </h3>
                            <div class="space-y-6">
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">15:30</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">DJ Synth</h4>
                                        <p class="text-white/70 text-sm">浩室音乐</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">18:00</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Bass Droppers</h4>
                                        <p class="text-white/70 text-sm">重低音</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">20:30</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Techno Titans</h4>
                                        <p class="text-white/70 text-sm">科技舞曲</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- 第二天 (默认隐藏) -->
                <div id="day2" class="schedule-day hidden">
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                        <!-- 主舞台 -->
                        <div class="bg-dark/50 backdrop-blur-lg p-8 rounded-2xl border border-white/10">
                            <h3 class="text-xl font-bold mb-6 flex items-center">
                                <span class="w-3 h-3 rounded-full bg-primary mr-2"></span>
                                主舞台
                            </h3>
                            <div class="space-y-6">
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">16:00</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Velvet Thunder</h4>
                                        <p class="text-white/70 text-sm">独立摇滚</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">18:30</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Crystal Echoes</h4>
                                        <p class="text-white/70 text-sm">梦幻流行</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">21:00</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Midnight Jazz</h4>
                                        <p class="text-white/70 text-sm">爵士融合</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 嘻哈舞台 -->
                        <div class="bg-dark/50 backdrop-blur-lg p-8 rounded-2xl border border-white/10">
                            <h3 class="text-xl font-bold mb-6 flex items-center">
                                <span class="w-3 h-3 rounded-full bg-accent mr-2"></span>
                                嘻哈舞台
                            </h3>
                            <div class="space-y-6">
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">15:30</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Rhythm Masters</h4>
                                        <p class="text-white/70 text-sm">嘻哈说唱</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">18:00</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Flow State</h4>
                                        <p class="text-white/70 text-sm">另类嘻哈</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">20:30</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Urban Poets</h4>
                                        <p class="text-white/70 text-sm">说唱诗歌</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- 第三天 (默认隐藏) -->
                <div id="day3" class="schedule-day hidden">
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                        <!-- 主舞台 -->
                        <div class="bg-dark/50 backdrop-blur-lg p-8 rounded-2xl border border-white/10">
                            <h3 class="text-xl font-bold mb-6 flex items-center">
                                <span class="w-3 h-3 rounded-full bg-primary mr-2"></span>
                                主舞台
                            </h3>
                            <div class="space-y-6">
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">16:00</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Harmonic Fusion</h4>
                                        <p class="text-white/70 text-sm">世界音乐</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">18:30</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Sonic Pioneers</h4>
                                        <p class="text-white/70 text-sm">实验音乐</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">21:00</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Final Horizon</h4>
                                        <p class="text-white/70 text-sm">电子摇滚</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 民谣舞台 -->
                        <div class="bg-dark/50 backdrop-blur-lg p-8 rounded-2xl border border-white/10">
                            <h3 class="text-xl font-bold mb-6 flex items-center">
                                <span class="w-3 h-3 rounded-full bg-green-400 mr-2"></span>
                                民谣舞台
                            </h3>
                            <div class="space-y-6">
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">15:30</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Acoustic Stories</h4>
                                        <p class="text-white/70 text-sm">原声民谣</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">18:00</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Folk Revolution</h4>
                                        <p class="text-white/70 text-sm">现代民谣</p>
                                    </div>
                                </div>
                                <div class="flex">
                                    <div class="w-24 text-right pr-4">
                                        <span class="text-secondary font-medium">20:30</span>
                                    </div>
                                    <div class="flex-1 pl-4 border-l-2 border-white/10">
                                        <h4 class="font-semibold">Country Roads</h4>
                                        <p class="text-white/70 text-sm">乡村音乐</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 艺人介绍 -->
    <section id="artists" class="py-24 bg-gradient-to-b from-dark/95 to-dark">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto text-center mb-16">
                <h2 class="text-[clamp(1.8rem,5vw,3rem)] font-bold mb-6">
                    <span class="bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">艺人阵容</span>
                </h2>
                <p class="text-white/80 text-lg leading-relaxed">
                    来自全球各地的顶尖音乐人，带来不同风格的音乐盛宴。点击播放按钮，提前感受他们的音乐魅力。
                </p>
            </div>
            
            <!-- 艺人过滤器 -->
            <div class="flex flex-wrap justify-center gap-4 mb-12">
                <button class="artist-filter-btn active px-6 py-2 rounded-full font-medium text-sm transition-all" data-filter="all">
                    全部艺人
                </button>
                <button class="artist-filter-btn px-6 py-2 rounded-full font-medium text-sm transition-all" data-filter="electronic">
                    电子音乐
                </button>
                <button class="artist-filter-btn px-6 py-2 rounded-full font-medium text-sm transition-all" data-filter="rock">
                    摇滚
                </button>
                <button class="artist-filter-btn px-6 py-2 rounded-full font-medium text-sm transition-all" data-filter="hiphop">
                    嘻哈
                </button>
                <button class="artist-filter-btn px-6 py-2 rounded-full font-medium text-sm transition-all" data-filter="folk">
                    民谣
                </button>
            </div>
            
            <!-- 艺人列表 -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- 艺人1 -->
                <div class="artist-card group" data-category="electronic">
                    <div class="relative overflow-hidden rounded-2xl">
                        <img src="https://p3-flow-imagex-sign.byteimg.com/tos-cn-i-a9rns2rl98/rc/pc/code_assistant/4707ed71afab458484cc89bd6b2bfd6c~tplv-a9rns2rl98-image.image?rk3s=8e244e95&amp;rrcfp=2609e108&amp;x-expires=1751723888&amp;x-signature=NkTREl4KqOSsC64lWDpEFQswsOs%3D" alt="Neon Horizon乐队照片" class="w-full h-80 object-cover transition-transform duration-500 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-dark via-dark/50 to-transparent"></div>
                        
                        <!-- 播放按钮 -->
                        <button class="music-play-btn absolute bottom-4 right-4 w-12 h-12 rounded-full bg-primary/80 backdrop-blur-sm flex items-center justify-center transition-all hover:bg-primary">
                            <i class="fa fa-play text-white"></i>
                        </button>
                        
                        <!-- 艺人信息 -->
                        <div class="absolute bottom-0 left-0 right-0 p-6">
                            <h3 class="text-xl font-bold">Neon Horizon</h3>
                            <p class="text-white/70 text-sm">电子流行</p>
                        </div>
                    </div>
                    
                    <!-- 艺人描述 (默认隐藏) -->
                    <div class="artist-details hidden mt-4 p-6 bg-dark/50 backdrop-blur-lg rounded-2xl border border-white/10">
                        <p class="text-white/80 mb-4">
                            Neon Horizon是一支来自瑞典的电子流行乐队，以其充满活力的现场表演和富有感染力的旋律而闻名。他们的音乐融合了合成器流行、电子舞曲和独立流行元素。
                        </p>
                        <div class="flex gap-3">
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-spotify"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-youtube-play"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-instagram"></i></a>
                        </div>
                    </div>
                </div>
                
                <!-- 艺人2 -->
                <div class="artist-card group" data-category="rock">
                    <div class="relative overflow-hidden rounded-2xl">
                        <img src="https://p9-flow-imagex-sign.byteimg.com/tos-cn-i-a9rns2rl98/rc/pc/code_assistant/244e79c636b54273bbc23bb4db3952fe~tplv-a9rns2rl98-image.image?rk3s=8e244e95&amp;rrcfp=2609e108&amp;x-expires=1751723906&amp;x-signature=HvJvrKhPGLBxPTT40%2BBQ228eTUo%3D" alt="Cosmic Waves乐队照片" class="w-full h-80 object-cover transition-transform duration-500 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-dark via-dark/50 to-transparent"></div>
                        
                        <!-- 播放按钮 -->
                        <button class="music-play-btn absolute bottom-4 right-4 w-12 h-12 rounded-full bg-primary/80 backdrop-blur-sm flex items-center justify-center transition-all hover:bg-primary">
                            <i class="fa fa-play text-white"></i>
                        </button>
                        
                        <!-- 艺人信息 -->
                        <div class="absolute bottom-0 left-0 right-0 p-6">
                            <h3 class="text-xl font-bold">Cosmic Waves</h3>
                            <p class="text-white/70 text-sm">迷幻摇滚</p>
                        </div>
                    </div>
                    
                    <!-- 艺人描述 (默认隐藏) -->
                    <div class="artist-details hidden mt-4 p-6 bg-dark/50 backdrop-blur-lg rounded-2xl border border-white/10">
                        <p class="text-white/80 mb-4">
                            Cosmic Waves是一支来自英国的迷幻摇滚乐队，以其大气磅礴的音景和引人深思的歌词而受到赞誉。他们的音乐融合了60年代迷幻摇滚和现代独立摇滚的元素。
                        </p>
                        <div class="flex gap-3">
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-spotify"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-youtube-play"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-instagram"></i></a>
                        </div>
                    </div>
                </div>
                
                <!-- 艺人3 -->
                <div class="artist-card group" data-category="hiphop">
                    <div class="relative overflow-hidden rounded-2xl">
                        <img src="https://p9-flow-imagex-sign.byteimg.com/tos-cn-i-a9rns2rl98/rc/pc/code_assistant/6f04700b8ffc4100bc377445d1b7bacd~tplv-a9rns2rl98-image.image?rk3s=8e244e95&amp;rrcfp=2609e108&amp;x-expires=1751723926&amp;x-signature=yiv9%2Fh0Cxopg21n29ihtGEyPmB4%3D" alt="Flow State乐队照片" class="w-full h-80 object-cover transition-transform duration-500 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-dark via-dark/50 to-transparent"></div>
                        
                        <!-- 播放按钮 -->
                        <button class="music-play-btn absolute bottom-4 right-4 w-12 h-12 rounded-full bg-primary/80 backdrop-blur-sm flex items-center justify-center transition-all hover:bg-primary">
                            <i class="fa fa-play text-white"></i>
                        </button>
                        
                        <!-- 艺人信息 -->
                        <div class="absolute bottom-0 left-0 right-0 p-6">
                            <h3 class="text-xl font-bold">Flow State</h3>
                            <p class="text-white/70 text-sm">另类嘻哈</p>
                        </div>
                    </div>
                    
                    <!-- 艺人描述 (默认隐藏) -->
                    <div class="artist-details hidden mt-4 p-6 bg-dark/50 backdrop-blur-lg rounded-2xl border border-white/10">
                        <p class="text-white/80 mb-4">
                            Flow State是来自美国的另类嘻哈组合，以其创新的节拍和富有诗意的歌词而著称。他们的音乐融合了嘻哈、电子和实验音乐元素，创造出独特的声音。
                        </p>
                        <div class="flex gap-3">
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-spotify"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-youtube-play"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-instagram"></i></a>
                        </div>
                    </div>
                </div>
                
                <!-- 艺人4 -->
                <div class="artist-card group" data-category="folk">
                    <div class="relative overflow-hidden rounded-2xl">
                        <img src="https://p3-flow-imagex-sign.byteimg.com/tos-cn-i-a9rns2rl98/rc/pc/code_assistant/0b3bf098460c4137b8de8fc021729a23~tplv-a9rns2rl98-image.image?rk3s=8e244e95&amp;rrcfp=2609e108&amp;x-expires=1751723944&amp;x-signature=yfD8xPlD1bJYX2YauVPQgCEnVxI%3D" alt="Acoustic Stories乐队照片" class="w-full h-80 object-cover transition-transform duration-500 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-dark via-dark/50 to-transparent"></div>
                        
                        <!-- 播放按钮 -->
                        <button class="music-play-btn absolute bottom-4 right-4 w-12 h-12 rounded-full bg-primary/80 backdrop-blur-sm flex items-center justify-center transition-all hover:bg-primary">
                            <i class="fa fa-play text-white"></i>
                        </button>
                        
                        <!-- 艺人信息 -->
                        <div class="absolute bottom-0 left-0 right-0 p-6">
                            <h3 class="text-xl font-bold">Acoustic Stories</h3>
                            <p class="text-white/70 text-sm">原声民谣</p>
                        </div>
                    </div>
                    
                    <!-- 艺人描述 (默认隐藏) -->
                    <div class="artist-details hidden mt-4 p-6 bg-dark/50 backdrop-blur-lg rounded-2xl border border-white/10">
                        <p class="text-white/80 mb-4">
                            Acoustic Stories是一个来自澳大利亚的民谣二重奏组合，以其温暖的和声和真挚的歌词而闻名。他们的音乐融合了传统民谣和现代创作技巧，创造出温馨而动人的听觉体验。
                        </p>
                        <div class="flex gap-3">
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-spotify"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-youtube-play"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-instagram"></i></a>
                        </div>
                    </div>
                </div>
                
                <!-- 艺人5 -->
                <div class="artist-card group" data-category="electronic">
                    <div class="relative overflow-hidden rounded-2xl">
                        <img src="https://p3-flow-imagex-sign.byteimg.com/tos-cn-i-a9rns2rl98/rc/pc/code_assistant/623c52a7511840c7aef42aff92269c92~tplv-a9rns2rl98-image.image?rk3s=8e244e95&amp;rrcfp=2609e108&amp;x-expires=1751723984&amp;x-signature=cOLlo1j5TBlvrcji3YCKln0QKS8%3D" alt="Techno Titans乐队照片" class="w-full h-80 object-cover transition-transform duration-500 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-dark via-dark/50 to-transparent"></div>
                        
                        <!-- 播放按钮 -->
                        <button class="music-play-btn absolute bottom-4 right-4 w-12 h-12 rounded-full bg-primary/80 backdrop-blur-sm flex items-center justify-center transition-all hover:bg-primary">
                            <i class="fa fa-play text-white"></i>
                        </button>
                        
                        <!-- 艺人信息 -->
                        <div class="absolute bottom-0 left-0 right-0 p-6">
                            <h3 class="text-xl font-bold">Techno Titans</h3>
                            <p class="text-white/70 text-sm">科技舞曲</p>
                        </div>
                    </div>
                    
                    <!-- 艺人描述 (默认隐藏) -->
                    <div class="artist-details hidden mt-4 p-6 bg-dark/50 backdrop-blur-lg rounded-2xl border border-white/10">
                        <p class="text-white/80 mb-4">
                            Techno Titans是一支来自德国的科技舞曲团队，以其复杂的节拍和前沿的电子音效而闻名。他们的音乐融合了Techno、House和Trance元素，创造出沉浸式的听觉体验。
                        </p>
                        <div class="flex gap-3">
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-spotify"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-youtube-play"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-instagram"></i></a>
                        </div>
                    </div>
                </div>
                
                <!-- 艺人6 -->
                <div class="artist-card group" data-category="rock">
                    <div class="relative overflow-hidden rounded-2xl">
                        <img src="https://p3-flow-imagex-sign.byteimg.com/tos-cn-i-a9rns2rl98/rc/pc/code_assistant/5d5dd154affd4eaa9cb26e490673401e~tplv-a9rns2rl98-image.image?rk3s=8e244e95&amp;rrcfp=2609e108&amp;x-expires=1751724001&amp;x-signature=MtvPUs%2FxNi0xkPgMk327mb5OW7k%3D" alt="Velvet Thunder乐队照片" class="w-full h-80 object-cover transition-transform duration-500 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-dark via-dark/50 to-transparent"></div>
                        
                        <!-- 播放按钮 -->
                        <button class="music-play-btn absolute bottom-4 right-4 w-12 h-12 rounded-full bg-primary/80 backdrop-blur-sm flex items-center justify-center transition-all hover:bg-primary">
                            <i class="fa fa-play text-white"></i>
                        </button>
                        
                        <!-- 艺人信息 -->
                        <div class="absolute bottom-0 left-0 right-0 p-6">
                            <h3 class="text-xl font-bold">Velvet Thunder</h3>
                            <p class="text-white/70 text-sm">独立摇滚</p>
                        </div>
                    </div>
                    
                    <!-- 艺人描述 (默认隐藏) -->
                    <div class="artist-details hidden mt-4 p-6 bg-dark/50 backdrop-blur-lg rounded-2xl border border-white/10">
                        <p class="text-white/80 mb-4">
                            Velvet Thunder是一支来自美国的独立摇滚乐队，以其充满活力的现场表演和富有感染力的旋律而闻名。他们的音乐融合了经典摇滚和现代独立音乐元素，创造出独特的声音。
                        </p>
                        <div class="flex gap-3">
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-spotify"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-youtube-play"></i></a>
                            <a href="#" class="text-white/70 hover:text-secondary"><i class="fa fa-instagram"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 购票选座 -->
    <section id="tickets" class="py-24 bg-dark">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto text-center mb-16">
                <h2 class="text-[clamp(1.8rem,5<h2 class="text-[clamp(1.8rem,5vw,3rem)] font-bold mb-6">
                    <span class="bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">购票选座</span>
                </h2>
                <p class="text-white/80 text-lg leading-relaxed">
                    选择您喜欢的票种和座位，开启三天的音乐之旅。早鸟票数量有限，先到先得！
                </p>
            </div>
            
            <!-- 票种选择 -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
                <!-- 普通票 -->
                <div class="bg-dark/50 backdrop-blur-lg rounded-2xl border border-white/10 overflow-hidden transition-transform hover:transform hover:scale-105">
                    <div class="bg-primary/20 p-4 text-center">
                        <h3 class="text-xl font-bold">普通票</h3>
                    </div>
                    <div class="p-8">
                        <div class="text-center mb-6">
                            <div class="text-4xl font-bold">¥888</div>
                            <p class="text-white/70">单人三日通票</p>
                        </div>
                        
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>三天音乐节全体验</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>所有舞台无障碍通行</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>官方周边购买资格</span>
                            </li>
                            <li class="flex items-start text-white/50">
                                <i class="fa fa-times text-red-400 mt-1 mr-3"></i>
                                <span>专属休息区</span>
                            </li>
                            <li class="flex items-start text-white/50">
                                <i class="fa fa-times text-red-400 mt-1 mr-3"></i>
                                <span>艺人见面会</span>
                            </li>
                        </ul>
                        
                        <button class="w-full py-3 rounded-lg bg-primary hover:bg-primary/90 transition-colors font-medium">
                            选择此票
                        </button>
                    </div>
                </div>
                
                <!-- VIP票 -->
                <div class="bg-dark/50 backdrop-blur-lg rounded-2xl border-2 border-secondary relative overflow-hidden transition-transform hover:transform hover:scale-105">
                    <div class="absolute top-0 right-0 bg-secondary text-dark px-4 py-1 text-sm font-medium">
                        最受欢迎
                    </div>
                    <div class="bg-secondary/20 p-4 text-center">
                        <h3 class="text-xl font-bold">VIP票</h3>
                    </div>
                    <div class="p-8">
                        <div class="text-center mb-6">
                            <div class="text-4xl font-bold">¥1688</div>
                            <p class="text-white/70">单人三日通票</p>
                        </div>
                        
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>三天音乐节全体验</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>所有舞台无障碍通行</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>官方周边购买资格</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>专属休息区</span>
                            </li>
                            <li class="flex items-start text-white/50">
                                <i class="fa fa-times text-red-400 mt-1 mr-3"></i>
                                <span>艺人见面会</span>
                            </li>
                        </ul>
                        
                        <button class="w-full py-3 rounded-lg bg-secondary text-dark hover:bg-secondary/90 transition-colors font-medium">
                            选择此票
                        </button>
                    </div>
                </div>
                
                <!-- 豪华票 -->
                <div class="bg-dark/50 backdrop-blur-lg rounded-2xl border border-white/10 overflow-hidden transition-transform hover:transform hover:scale-105">
                    <div class="bg-accent/20 p-4 text-center">
                        <h3 class="text-xl font-bold">豪华票</h3>
                    </div>
                    <div class="p-8">
                        <div class="text-center mb-6">
                            <div class="text-4xl font-bold">¥2888</div>
                            <p class="text-white/70">单人三日通票</p>
                        </div>
                        
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>三天音乐节全体验</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>所有舞台无障碍通行</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>官方周边购买资格</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>专属休息区</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fa fa-check text-green-400 mt-1 mr-3"></i>
                                <span>艺人见面会</span>
                            </li>
                        </ul>
                        
                        <button class="w-full py-3 rounded-lg bg-accent hover:bg-accent/90 transition-colors font-medium">
                            选择此票
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- 座位选择区域 -->
            <div class="bg-dark/50 backdrop-blur-lg p-8 rounded-2xl border border-white/10">
                <h3 class="text-xl font-bold mb-6">选择座位区域</h3>
                
                <!-- 座位图 -->
                <div class="relative w-full h-96 mb-8">
                    <svg viewBox="0 0 800 400" class="w-full h-full">
                        <!-- 舞台 -->
                        <rect x="200" y="20" width="400" height="60" rx="10" fill="#6C2BD9"></rect>
                        <text x="400" y="55" text-anchor="middle" fill="white" font-size="18">舞台</text>
                        
                        <!-- A区 -->
                        <rect x="100" y="100" width="600" height="100" rx="5" fill="#00E5FF" fill-opacity="0.2" stroke="#00E5FF" stroke-width="2" class="cursor-pointer hover:fill-opacity-0.4 transition-opacity"></rect>
                        <text x="400" y="160" text-anchor="middle" fill="white" font-size="16">A区 - 普通票</text>
                        
                        <!-- B区 -->
                        <rect x="150" y="220" width="500" height="100" rx="5" fill="#FF00FF" fill-opacity="0.2" stroke="#FF00FF" stroke-width="2" class="cursor-pointer hover:fill-opacity-0.4 transition-opacity"></rect>
                        <text x="400" y="280" text-anchor="middle" fill="white" font-size="16">B区 - VIP票</text>
                        
                        <!-- C区 -->
                        <rect x="200" y="340" width="400" height="50" rx="5" fill="#6C2BD9" fill-opacity="0.2" stroke="#6C2BD9" stroke-width="2" class="cursor-pointer hover:fill-opacity-0.4 transition-opacity"></rect>
                        <text x="400" y="370" text-anchor="middle" fill="white" font-size="14">C区 - 豪华票</text>
                    </svg>
                </div>
                
                <!-- 座位图例 -->
                <div class="flex flex-wrap gap-6 mb-8">
                    <div class="flex items-center">
                        <div class="w-4 h-4 bg-primary/20 border border-primary rounded-sm mr-2"></div>
                        <span class="text-sm text-white/70">豪华票区域</span>
                    </div>
                    <div class="flex items-center">
                        <div class="w-4 h-4 bg-secondary/20 border border-secondary rounded-sm mr-2"></div>
                        <span class="text-sm text-white/70">普通票区域</span>
                    </div>
                    <div class="flex items-center">
                        <div class="w-4 h-4 bg-accent/20 border border-accent rounded-sm mr-2"></div>
                        <span class="text-sm text-white/70">VIP票区域</span>
                    </div>
                    <div class="flex items-center">
                        <div class="w-4 h-4 bg-red-500/20 border border-red-500 rounded-sm mr-2"></div>
                        <span class="text-sm text-white/70">已售座位</span>
                    </div>
                </div>
                
                <!-- 购票表单 -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-white/80 mb-2">选择票种</label>
                        <select class="w-full bg-dark/70 border border-white/20 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-secondary">
                            <option>普通票 - ¥888</option>
                            <option>VIP票 - ¥1688</option>
                            <option>豪华票 - ¥2888</option>
                        </select>
                    </div>
                    
                    <div>
                        <label class="block text-white/80 mb-2">票数</label>
                        <div class="flex items-center">
                            <button class="w-10 h-10 bg-dark/70 border border-white/20 rounded-l-lg flex items-center justify-center">-</button>
                            <input type="number" value="1" min="1" max="10" class="w-16 h-10 bg-dark/70 border-y border-white/20 text-center text-white">
                            <button class="w-10 h-10 bg-dark/70 border border-white/20 rounded-r-lg flex items-center justify-center">+</button>
                        </div>
                    </div>
                    
                    <div class="md:col-span-2">
                        <label class="block text-white/80 mb-2">选择日期</label>
                        <div class="flex flex-wrap gap-3">
                            <label class="flex items-center">
                                <input type="checkbox" class="mr-2 accent-primary">
                                <span>7月15日</span>
                            </label>
                            <label class="flex items-center">
                                <input type="checkbox" class="mr-2 accent-primary">
                                <span>7月16日</span>
                            </label>
                            <label class="flex items-center">
                                <input type="checkbox" class="mr-2 accent-primary">
                                <span>7月17日</span>
                            </label>
                            <label class="flex items-center">
                                <input type="checkbox" class="mr-2 accent-primary" checked="">
                                <span>三日通票</span>
                            </label>
                        </div>
                    </div>
                    
                    <div class="md:col-span-2">
                        <button class="w-full py-4 rounded-lg bg-gradient-to-r from-primary to-secondary hover:opacity-90 transition-opacity font-bold text-lg">
                            确认购票
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 倒计时开抢提醒 -->
    <section class="py-16 bg-gradient-to-r from-primary/20 to-secondary/20">
        <div class="container mx-auto px-4 text-center">
            <h2 class="text-3xl md:text-4xl font-bold mb-8">早鸟票倒计时</h2>
            <div class="flex justify-center gap-4 mb-8">
                <div class="bg-dark/70 backdrop-blur-xl p-4 rounded-xl border border-white/10 w-20 md:w-28">
                    <div id="countdown-days" class="text-2xl md:text-4xl font-bold text-secondary">05</div>
                    <div class="text-xs md:text-sm text-white/70 mt-1">天</div>
                </div>
                <div class="bg-dark/70 backdrop-blur-xl p-4 rounded-xl border border-white/10 w-20 md:w-28">
                    <div id="countdown-hours" class="text-2xl md:text-4xl font-bold text-secondary">12</div>
                    <div class="text-xs md:text-sm text-white/70 mt-1">时</div>
                </div>
                <div class="bg-dark/70 backdrop-blur-xl p-4 rounded-xl border border-white/10 w-20 md:w-28">
                    <div id="countdown-minutes" class="text-2xl md:text-4xl font-bold text-secondary">30</div>
                    <div class="text-xs md:text-sm text-white/70 mt-1">分</div>
                </div>
                <div class="bg-dark/70 backdrop-blur-xl p-4 rounded-xl border border-white/10 w-20 md:w-28">
                    <div id="countdown-seconds" class="text-2xl md:text-4xl font-bold text-secondary">45</div>
                    <div class="text-xs md:text-sm text-white/70 mt-1">秒</div>
                </div>
            </div>
            <p class="text-white/80 mb-8">早鸟票限时优惠，数量有限，先到先得！</p>
            <button class="bg-white text-primary px-8 py-4 rounded-full font-bold hover-scale">
                订阅提醒
            </button>
        </div>
    </section>

    <!-- 页脚 -->
    <footer class="bg-dark py-12">
        <div class="container mx-auto px-4">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
                <div>
                    <a href="#" class="flex items-center gap-2 mb-4">
                        <div class="w-10 h-10 rounded-full bg-gradient-to-r from-primary to-secondary flex items-center justify-center">
                            <i class="fa fa-music text-white"></i>
                        </div>
                        <span class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">SoundWave</span>
                    </a>
                    <p class="text-white/70 mb-4">
                        2025年7月15-17日 · 上海世博公园
                    </p>
                    <div class="flex gap-4">
                        <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-primary/20 transition-colors">
                            <i class="fa fa-facebook text-white"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-primary/20 transition-colors">
                            <i class="fa fa-twitter text-white"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-primary/20 transition-colors">
                            <i class="fa fa-instagram text-white"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-primary/20 transition-colors">
                            <i class="fa fa-youtube-play text-white"></i>
                        </a>
                    </div>
                </div>
                
                <div>
                    <h3 class="text-lg font-bold mb-4">快速链接</h3>
                    <ul class="space-y-2">
                        <li><a href="#about" class="text-white/70 hover:text-secondary transition-colors">关于</a></li>
                        <li><a href="#schedule" class="text-white/70 hover:text-secondary transition-colors">时间表</a></li>
                        <li><a href="#artists" class="text-white/70 hover:text-secondary transition-colors">艺人阵容</a></li>
                        <li><a href="#tickets" class="text-white/70 hover:text-secondary transition-colors">购票选座</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3 class="text-lg font-bold mb-4">帮助</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-white/70 hover:text-secondary transition-colors">常见问题</a></li>
                        <li><a href="#" class="text-white/70 hover:text-secondary transition-colors">场馆信息</a></li>
                        <li><a href="#" class="text-white/70 hover:text-secondary transition-colors">交通指南</a></li>
                        <li><a href="#" class="text-white/70 hover:text-secondary transition-colors">联系我们</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3 class="text-lg font-bold mb-4">订阅最新消息</h3>
                    <p class="text-white/70 mb-4">获取音乐节最新动态和独家优惠</p>
                    <div class="flex">
                        <input type="email" placeholder="您的邮箱地址" class="bg-dark/70 border border-white/20 rounded-l-lg px-4 py-2 text-white flex-1 focus:
