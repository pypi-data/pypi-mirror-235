# @gradio/tabs

## 0.1.0-beta.6

### Features

- [#5960](https://github.com/gradio-app/gradio/pull/5960) [`319c30f3f`](https://github.com/gradio-app/gradio/commit/319c30f3fccf23bfe1da6c9b132a6a99d59652f7) - rererefactor frontend files.  Thanks [@pngwn](https://github.com/pngwn)!
- [#5938](https://github.com/gradio-app/gradio/pull/5938) [`13ed8a485`](https://github.com/gradio-app/gradio/commit/13ed8a485d5e31d7d75af87fe8654b661edcca93) - V4: Use beta release versions for '@gradio' packages.  Thanks [@freddyaboulton](https://github.com/freddyaboulton)!

## 0.0.7

### Patch Changes

- Updated dependencies []:
  - @gradio/utils@0.1.2

## 0.0.6

### Features

- [#5590](https://github.com/gradio-app/gradio/pull/5590) [`d1ad1f671`](https://github.com/gradio-app/gradio/commit/d1ad1f671caef9f226eb3965f39164c256d8615c) - Attach `elem_classes` selectors to layout elements, and an id to the Tab button (for targeting via CSS/JS). Thanks [@abidlabs](https://github.com/abidlabs)!

## 0.0.5

### Patch Changes

- Updated dependencies []:
  - @gradio/utils@0.1.1

## 0.0.4

### Patch Changes

- Updated dependencies [[`abf1c57d`](https://github.com/gradio-app/gradio/commit/abf1c57d7d85de0df233ee3b38aeb38b638477db)]:
  - @gradio/utils@0.1.0

## 0.0.3

### Highlights

#### Improve startup performance and markdown support ([#5279](https://github.com/gradio-app/gradio/pull/5279) [`fe057300`](https://github.com/gradio-app/gradio/commit/fe057300f0672c62dab9d9b4501054ac5d45a4ec))

##### Improved markdown support

We now have better support for markdown in `gr.Markdown` and `gr.Dataframe`. Including syntax highlighting and Github Flavoured Markdown. We also have more consistent markdown behaviour and styling.

##### Various performance improvements

These improvements will be particularly beneficial to large applications.

- Rather than attaching events manually, they are now delegated, leading to a significant performance improvement and addressing a performance regression introduced in a recent version of Gradio. App startup for large applications is now around twice as fast.
- Optimised the mounting of individual components, leading to a modest performance improvement during startup (~30%).
- Corrected an issue that was causing markdown to re-render infinitely.
- Ensured that the `gr.3DModel` does re-render prematurely.

Thanks [@pngwn](https://github.com/pngwn)!

## 0.0.2

### Patch Changes

- Updated dependencies []:
  - @gradio/utils@0.0.2