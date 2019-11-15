from django.db import models
from django.db.models import Q, F, Count, Avg, Max, Min


class Publisher(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Egg(models.Model):
    name = models.CharField(max_length=10)


class Spam(models.Model):
    name = models.CharField(max_length=10)
    eggs = models.ManyToManyField(Egg)


class Article(models.Model):

    CATEGORIES = (
        ('f', 'foo'),
        ('b', 'bar'),
        ('s', 'spam'),
        ('e', 'eggs'),
    )

    name = models.CharField(max_length=200)
    body = models.TextField()
    category = models.CharField(max_length=1, choices=CATEGORIES)

    publisher = models.ForeignKey(Publisher, models.CASCADE)

    @property
    def body_short(self):
        if len(self.body) > 20:
            return f'{self.body[:20]}...'
        return self.body

    def __str__(self):
        return f'{self.name!r}: {self.body_short}'


if __name__ == '__main__':
    from otusblog.models import Publisher, Article, Egg, Spam
    Article.objects.filter(category='f')
    Article.objects.filter(category='foo')
    a.publisher
    p.article_set.filter()
    p.article_set.filter(name__startswith='flask')
    p.article_set.filter(name__contains='flask')
    from django.db.models import Q

    Q()
    Q(qwe='123')
    Q(qwe='123', abc=123)
    Q(qwe='123') | Q(abc=123)
    Article.objects.filter(id__in=[1, 2])
    Article.objects.filter(Q(publisher__first_name='John'))
    Article.objects.aggregate(num_articles=Count('id'))
    p.article_set.aggregate(num_articles=Count('id'))
    Article.objects.aggregate(avg_id=Avg('id'))
    Article.objects.aggregate(Avg('id'), Max('id'), Min('id'))
    Article.objects.annotate(Count('publisher'))

    s = Spam.objects.create()
    s.eggs.set([e1,e2])
    s.eggs.all()