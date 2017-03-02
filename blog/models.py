from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField


class CodeBlockPython(blocks.TextBlock):
    class Meta:
        template = 'blog/code_python.html'
        icon = 'code'
        label = 'Code Python'


class CodeBlockNoHighlight(blocks.TextBlock):
    class Meta:
        template = 'blog/code_nohighlight.html'
        icon = 'code'
        label = 'Code No Highlight'


class AllBlogsIndexPage(Page):
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(AllBlogsIndexPage, self).get_context(request)

        blogindexpages = self.get_children().live().filter(blogindexpage__most_recent_post_first__isnull = False)

        for blogindexpage in blogindexpages:
            # Only blog index pages will succeed in try clause
            try:
                if blogindexpage.specific.most_recent_post_first:
                    blogpages = blogindexpage.get_children().live().order_by('-blogpage__date', '-first_published_at')
                else:
                    blogpages = blogindexpage.get_children().live().order_by('blogpage__date', 'first_published_at')
                blogindexpage.blogpages = blogpages
            except:
                pass

        context['blogindexpages'] = blogindexpages

        return context


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    most_recent_post_first = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('most_recent_post_first', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)
        if self.most_recent_post_first:
            blogpages = self.get_children().live().order_by('-blogpage__date', '-first_published_at')
        else:
            blogpages = self.get_children().live().order_by('blogpage__date', 'first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full")
    ]


class BlogPageWithCode(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, blank=True)
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('code_python', CodeBlockPython()),
        ('code_nohighlight', CodeBlockNoHighlight()),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML'))
    ])

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body')
    ]
