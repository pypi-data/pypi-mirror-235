# Archive

Archives are a [`BasePage`][src.render_engine.page.BasePage] object used to display a list of [`Page`][src.render_engine.page.Page] objects in a [`Collection`][src.render_engine.collection.Collection].

Archive objects create a customizeable page that can be controlled via its parent Collction.

::: src.render_engine.archive.Archive

Collection.archives yields a generator of Archive objects. Each Archive object will have a `pages` attribute that is a list of Page objects referenced in that Archive Page. The number of pages is determined by the `Collection.items_per_page` attribute.

The slug of the Archive Page is determined by whether the Archive is paginated.

If there is more than one archive page, the Archive.archive_index will be appended to the Archive.slug . For example, if the Archive.slug is `archive` and the Archive.archive_index is `2`, the Archive Page will have a slug of `archive2`.
