# The /llms.txt file

## Background

Today websites are not just used to provide information to people, but they are also used to provide information to large language models. This can be used, for instance, in order to provide information necessary for coders to use a library, or as part of research to learn about a person or organization and so forth. Providing information for language models is a little different to providing information for humans, although there is plenty of overlap. Language models generally like to have information in a more concise form which can be more similar to what a human expert would want to read rather than a complete beginner to a topic. Language models can ingest a lot of information quickly. So it can be helpful to have a single place where all of the key information can be collated.

The llms.txt format can be used in various scenarios. For software libraries, it can provide a structured overview of documentation, making it easier for LLMs to locate specific features or usage examples. In corporate websites, it can outline organizational structure and key information sources. Information about new legislation and necessary background and context could be curated in an llms.txt file to help stakeholders understand it.

llms.txt can be adapted for various domains. Personal portfolio or CV websites could use it to help answer questions about an individual. In e-commerce, it could outline product categories and policies. Educational institutions might use it to summarize course offerings and resources.

At the moment the most widely and easily understood format for language models is Markdown. Simply showing where key Markdown files can be found is a great first step. Providing some basic structure helps a language model to find where the information it needs can come from.

## Format

The llms.txt file is unusual in that it uses Markdown to structure the information rather than a classic structured format such as XML. The reason for this is that we expect many of these files to be read by language models. Having said that, the information in llms.txt follows a specific format and can be read using standard programmatic-based tools.

The llms.txt file spec is for files located in the root path `/llms.txt` of a website (or, optionally, in a subpath). A file following the spec contains the following sections as markdown, in the specific order:

- An H1 with the name of the project or site. This is the only required section
- A blockquote with a short summary of the project, containing key information necessary for understanding the rest of the file
- Zero or more markdown sections (e.g. paragraphs, lists, etc) of any type, except headings, containing more detailed information about the project and how to interpret the provided files
- Zero or more markdown sections delimited by H2 headers, containing "file lists" of URLs where further detail is available
  - Each "file list" is a markdown list, containing a required markdown hyperlink `[name](url)`, then optionally a `:` and notes about the file.

## Existing standards

llms.txt is designed to coexist with current web standards. While sitemaps list all pages for search engines, llms.txt offers a curated overview for LLMs. It can complement robots.txt by providing context for allowed content. The file can also reference structured data markup used on the site, helping LLMs understand how to interpret this information in context.

The approach of standardising on a path for the file follows the approach of `/robots.txt` and `/sitemap.xml`. robots.txt and llms.txt have different purposes — llms.txt information would generally be explicitly requested by a human for a particular task, to have a language model help them use the information on a website. On the other hand, robots.txt is generally used to let automated tools what access to a site is considered acceptable.

sitemap.xml is a list of all the indexable human-readable information available on a site. This isn’t a substitute for llms.txt since it:

- Often won’t have the LLM-readable versions of pages listed
- Doesn’t include URLs to external sites, even although they might be helpful to understand the information
- Will generally cover documents that in aggregate will be too large to fit in an LLM context window, and will include a lot of information that isn’t necessary to understand the site.

## Example

Here’s an example of llms.txt, in this case a cut down version of the file used for the FastHTML project:

```markdown
# FastHTML

> FastHTML is a python library which brings together Starlette, Uvicorn, HTMX, and fastcore's `FT` "FastTags" into a library for creating server-rendered hypermedia applications.

FastHTML is written by Answer.AI, an organization which follows the fast.ai style guide instead of PEP 8, so most examples follow fast.ai style.

## Docs

- [FastHTML quick start](https://docs.fastht.ml/tutorials/quickstart_for_web_devs.html.md): A brief overview of many FastHTML features
- [HTMX reference](https://raw.githubusercontent.com/bigskysoftware/reference.md): Brief description of all HTMX attributes, CSS classes, headers, events, extensions, js lib methods, and config options

## Examples

- [Todo list application](https://raw.githubusercontent.com/AnswerDotAI/fasthtml/adv_app.py): Detailed walk-thru of a complete CRUD app in FastHTML showing idiomatic use of FastHTML and HTMX patterns.

## Optional

- [Starlette full documentation](https://gist.githubusercontent.com/jph00/starlette-sml.md): A subset of the Starlette documentation useful for FastHTML development.
```

To create effective llms.txt files, consider these guidelines: Use concise, clear language. When linking to resources, include brief, informative descriptions. Avoid ambiguous terms or unexplained jargon. Run a tool that expands your llms.txt file into an LLM context file and test a number of language models to see if they can answer questions about your content.

## Next steps

The llms.txt specification is open for community input. A GitHub repository hosts this informal overview, allowing for version control and public discussion. A community discord channel is available for sharing implementation experiences and discussing best practices.