import re
from django.shortcuts import render
from datetime import datetime
from .models import Post

MONTH_NAMES = ('', 'January', 'Feburary', 'March', 'April',
               'May', 'June', 'July', 'August', 'September',
               'October', 'November', 'December')


def frontpage(request):
    post, pagedata = init()
    pagedata.update({'subtitle': '', })
    return render('blog/listpage.html', pagedata)


def singlepost(request, year, month, slug2):
    posts, pagedata = init()
    post = posts.get(
                    date_created__year=year,
                    date_created__month=int(month),
                    slug=slug2,)
    pagedata.update({'post': post})
    return render('blog/singlepost.html', pagedata)


def yearview(request, year):
    posts, pagedata = init()
    posts = posts.filter(date_created__year=year)
    pagedata.update({'post_list': posts,
                    'subtitle': 'Posts for %s' % year})


def monthview(request, year, month):
    posts, pagedata = init()
    posts = posts.filter(date_created__year=year)
    posts = posts.filter(date_created__month=int(month))
    pagedata.update({
        'post_list': posts,
        'subtitle': 'Posts for %s %s' % (MONTH_NAMES[int(month)], year), })
    return render('blog/listpage.html', pagedata)


def tagview(request, tag):
    allposts, pagedata = init()
    posts = []
    for post in allposts:
        tags = re.split('', post.tags)
    if tag in tags:
        posts.append(post)
        pagedata.update({'post_list': posts,
                        'subtitle': "Posts tagged '%s'" % tag, })
    return render('blog/listpage.html', pagedata)


def create_tag_data(posts):
    tag_data = []
    count = {}
    for post in posts:
        tags = re.split(" ", post.tags)
    for tag in tags:
        if tag not in count:
            count[tag] = 1
        else:
            count[tag] += 1
    # for tag, count in sorted(count.items(), key=lambda tag: Post.tags):
    #     tag_data.append({'tag': tag,
    #                     'count': count, })
    return tag_data


def init():
    posts = Post.objects.all()
    tag_data = create_tag_data(posts)
    archieve_data = create_archieve_data(posts)
    pagedata = {'version': '0.0.1',
                'post_list': posts,
                'tag_counts': tag_data,
                'archieve_counts': archieve_data, }
    return posts, pagedata


def create_archieve_data(posts):
    archieve_data = []
    count = {}
    mcount = {}
    for post in posts:
        year = post.date_created.year
        month = post.date_created.month
        if year not in count:
            count[year] = 1
            mcount[year] = {}
        else:
            count[year] += 1
        if month not in mcount[year]:
            mcount[year][month] = 1
        else:
            mcount[year][month] += 1
    for year in sorted(count.items(), reverse=True):
        archieve_data.append({'isyear': True,
                              'year': year,
                              'count': count[year], })
        for month in sorted(mcount[year].items(), reverse=True):
            archieve_data.append({'isyear': False,
                                  'yearmonth': '%d/%02d' % (year, month),
                                  'monthname': MONTH_NAMES[month],
                                  'count': mcount[year][month], })
    return archieve_data
