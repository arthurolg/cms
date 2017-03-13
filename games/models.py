# coding=utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from taggit.managers import TaggableManager


def image_platform_upload_to(instance, filename):
    title = instance.name
    slug = slugify(title)
    filename = slugify(filename)
    return "platform/%s/%s" % (slug, filename)


class Platform(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to=image_platform_upload_to,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


def image_game_upload_to(instance, filename):
    title = instance.name
    slug = slugify(title)
    filename = slugify(filename)
    return "game/%s/%s" % (slug, filename)


class Game(models.Model):
    GENRE_GAMES = (
        ('NA', 'N/A'),
        ('ACT', 'Acción'),
        ('ADV', 'Aventura'),
        ('HOR', 'Horror'),
        ('SCI', 'Ciencia Ficción'),
    )
    TYPE_GAMES = (
        ('NA', 'N/A'),
        ('SHO', 'Shooter'),
        ('GEN', 'Generalidades'),
        ('FIG', 'Lucha'),
        ('BEU', 'Beat em up'),
        ('FPS', 'Disparos en primera persona'),
        ('TPS', 'Disparos en tercera persona'),
        ('EST', 'Estrategía'),
        ('SIM', 'Simulación'),
        ('SPO', 'Deporte'),
        ('RUN', 'Carreras'),
        ('ADV', 'Aventura'),
    )
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to=image_game_upload_to,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0, null=True)
    website = models.URLField(null=True, blank=True)
    release_date = models.DateField(null=True)
    engine = models.CharField(max_length=40, null=True, blank=True)
    type_game = models.CharField(max_length=3, choices=TYPE_GAMES, default='NA')
    genre = models.CharField(max_length=3, choices=GENRE_GAMES, default='NA')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game:detail", kwargs={"slug": self.slug})

    def get_image_url(self):
        img = self.picture_set.first()
        if img:
            return img.picture.url
        return self.image.url

    class Meta:
        ordering = ["-timestamp", "-updated"]


def image_game_launch_upload_to(instance, filename):
    if instance.game:
        title = instance.game.name
    elif instance.title:
        title = instance.title
    else:
        title = "preview"
    slug = slugify(title)
    filename = slugify(filename)
    return "game/%s/launch/%s" % (slug, filename)


class LaunchGame(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(upload_to=image_game_launch_upload_to,
                              null=False,
                              blank=False,
                              width_field="width_field",
                              height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    date = models.DateField()
    game = models.ForeignKey(Game, null=True, blank=True)

    def __unicode__(self):
        if self.game:
            title = self.game.name
        elif self.title:
            title = self.title
        else:
            title = self.image.name
        return title


def image_game_featured_upload_to(instance, filename):
    if instance.game:
        title = instance.game.name
    elif instance.title:
        title = instance.title
    else:
        title = "preview"
    slug = slugify(title)
    filename = slugify(filename)
    return "game/%s/featured/%s" % (slug, filename)


class FeaturedGame(models.Model):
    title = models.CharField(max_length=120)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to=image_game_featured_upload_to,
                              null=False,
                              blank=False,
                              width_field="width_field",
                              height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    game = models.ForeignKey(Game, null=True, blank=True)

    def __unicode__(self):
        if self.game:
            title = self.game.name
        elif self.title:
            title = self.title
        else:
            title = self.image.name
        return title


def image_news_upload_to(instance, filename):
    title = instance.title
    slug = slugify(title)
    filename = slugify(filename)
    return "news/%s/%s" % (slug, filename)


class News(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    excerpt = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to=image_news_upload_to,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    link = models.CharField(max_length=200)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("game:news_detail", kwargs={"slug": self.slug})

    def get_image_url(self):
        return self.image.url

    class Meta:
        ordering = ["-timestamp", "-updated"]


def image_video_upload_to(instance, filename):
    if instance.game:
        title = instance.game.name
    elif instance.title:
        title = instance.title
    else:
        title = instance.type_video
    slug = slugify(title)
    filename = slugify(filename)
    return "game/%s/videos/%s" % (slug, filename)


class Video(models.Model):
    TYPE_VIDEO = (
        ('NA', 'N/A'),
        ('GPL', 'Gameplay'),
        ('WLK', 'Walkthrough'),
        ('DMO', 'Demo'),
        ('TRA', 'Trailer'),
        ('GID', 'Guia'),
        ('TRC', 'Trucos y Secretos'),
    )
    game = models.ForeignKey(Game, null=True, blank=True)
    title = models.CharField(max_length=120)
    url_youtube = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to=image_video_upload_to,
                                       null=True,
                                       blank=True,
                                       width_field="width_field",
                                       height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    type_video = models.CharField(max_length=3, choices=TYPE_VIDEO, default='NA')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title


def image_image_upload_to(instance, filename):
    if instance.game:
        title = instance.game.name
    elif instance.title:
        title = instance.title
    else:
        title = "preview"
    slug = slugify(title)
    filename = slugify(filename)
    return "game/%s/images/%s" % (slug, filename)


class Picture(models.Model):
    game = models.ForeignKey(Game, null=True, blank=True)
    title = models.CharField(max_length=120)
    excerpt = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to=image_image_upload_to,
                                null=True,
                                blank=True,
                                width_field="width_field",
                                height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title


class GalleryGame(models.Model):
    title = models.CharField(max_length=120)
    pictures = models.ManyToManyField(Picture)
    videos = models.ManyToManyField(Video)
    show = models.BooleanField(default=True)
    game = models.ForeignKey(Game, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return "%s | '%s'" % (self.title, self.game.name)

OCCUPATIONS = (
    ('NA', 'N/A'),
    ('DEV', 'Desarrollador'),
    ('PUB', 'Publicista'),
    ('PRO', 'Productor'),
    ('DIS', 'Diseñador'),
)


class PersonIndustry(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    occupation = models.CharField(max_length=3, choices=OCCUPATIONS, default='NA')
    description = models.TextField(null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.name


class DeveloperGame(models.Model):
    game = models.ForeignKey(Game)
    person = models.ForeignKey(PersonIndustry)
    kind = models.CharField(max_length=3, choices=OCCUPATIONS)

    def __unicode__(self):
        return "%s | %s (%s)" % (self.person.name, self.game.name, self.kind)


def image_classification_upload_to(instance, filename):
    title = instance.name
    slug = slugify(title)
    filename = slugify(filename)
    return "game/classification/%s/%s" % (slug, filename)


class Classification(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=image_classification_upload_to,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)


class ClassificationGame(models.Model):
    game = models.ForeignKey(Game)
    classification = models.ForeignKey(Classification)

    def __unicode__(self):
        return "%s | %s" % (self.classification.name, self.game.name)


class PlatformGame(models.Model):
    game = models.ForeignKey(Game)
    platform = models.ForeignKey(Platform)

    def __unicode__(self):
        return "%s | %s" % (self.platform.name, self.game.name)


# Creacion de los campos slug para los modelos
def create_slug_classification(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Classification.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_classification(instance, new_slug=new_slug)
    return slug


def pre_save_classification_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_classification(instance)


def create_slug_person_industry(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = PersonIndustry.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_person_industry(instance, new_slug=new_slug)
    return slug


def pre_save_person_industry_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_person_industry(instance)


def create_slug_news(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = News.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_news(instance, new_slug=new_slug)
    return slug


def pre_save_news_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_news(instance)


def create_slug_game(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Game.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_game(instance, new_slug=new_slug)
    return slug


def pre_save_game_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_game(instance)


def create_slug_platform(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Platform.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_platform(instance, new_slug=new_slug)
    return slug


def pre_save_platform_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_platform(instance)


pre_save.connect(pre_save_game_receiver, sender=Game)

pre_save.connect(pre_save_platform_receiver, sender=Platform)

pre_save.connect(pre_save_news_receiver, sender=News)

pre_save.connect(pre_save_person_industry_receiver, sender=PersonIndustry)

pre_save.connect(pre_save_classification_receiver, sender=Classification)
