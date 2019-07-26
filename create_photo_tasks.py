from celery import Celery
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot as driver

app = Celery('hello', broker='redis://127.0.0.1:6379', backend='redis://127.0.0.1:6379')


@app.task
def snapshot_img(html_path, img_name):
    make_snapshot(driver, html_path, img_name)
    return 'hello world'

# make_snapshot(driver,"/home/wangkun/PycharmProjects/pyecharts_demo/render.html", "bar.png")
