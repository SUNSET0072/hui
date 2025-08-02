from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# 配置项目路径
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 确保上传文件夹存在
if not os.path.isdir(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 作品数据
portfolio_items = [
    {
        'id': 1,
        'title': '移动应用UI设计',
        'description': '现代简约风格的健康类应用界面设计',
        'image': 'https://picsum.photos/id/1/600/400',
        'category': 'design',
        'type': 'image'
    },
    {
        'id': 2,
        'title': '自然风景摄影',
        'description': '山川湖泊的壮丽景色捕捉',
        'image': 'https://picsum.photos/id/29/600/400',
        'category': 'photo',
        'type': 'image'
    },
    {
        'id': 3,
        'title': '城市宣传片',
        'description': '现代都市生活的精彩瞬间',
        'image': 'https://picsum.photos/id/96/600/400',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'category': 'video',
        'type': 'video'
    },
    {
        'id': 4,
        'title': '品牌视觉设计',
        'description': '餐饮品牌的全套视觉识别系统',
        'image': 'https://picsum.photos/id/3/600/400',
        'category': 'design',
        'type': 'image'
    },
    {
        'id': 5,
        'title': '人像摄影集',
        'description': '捕捉人物情感与个性的瞬间',
        'image': 'https://picsum.photos/id/65/600/400',
        'category': 'photo',
        'type': 'image'
    },
    {
        'id': 6,
        'title': '产品展示视频',
        'description': '高端电子产品的功能展示',
        'image': 'https://picsum.photos/id/119/600/400',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'category': 'video',
        'type': 'video'
    }
]

# 路由配置
@app.route('/')
def home():
    return render_template('index.html', 
                          portfolio_items=portfolio_items,
                          title='个人作品集 | Creative Portfolio')

@app.route('/about')
def about():
    return render_template('about.html', title='关于我 | Creative Portfolio')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='联系我 | Creative Portfolio')

@app.route('/portfolio/<int:item_id>')
def portfolio_item(item_id):
    item = next((item for item in portfolio_items if item['id'] == item_id), None)
    if item:
        return render_template('portfolio_item.html', item=item, title=f"{item['title']} | Creative Portfolio")
    return "作品不存在", 404

if __name__ == '__main__':
    app.run(debug=True)
