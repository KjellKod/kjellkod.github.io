# Projects

The things I build, and the thinking behind them — open source, spanning AI
orchestration, production-grade C++, and the engineering-leadership tools in
between.

<!--
To add a project: copy a card block inside the relevant section and edit the four
parts — icon, title, description, link. Cards use the Material "grid cards"
extension (attr_list + md_in_html); keep one blank line between cards.
-->

## AI orchestration & developer tooling

Where most of my current energy goes: tools that help agents and engineers do
trustworthy work — plan it, verify it against evidence, and ship it without the
guesswork.

<div class="grid cards" markdown>

-   :material-shield-check:{ .lg .middle } __RepoLens__

    ---

    Know exactly what open source you ship — and what it obligates you to. A
    license-disclosure orchestrator that verifies licenses against authoritative
    sources and turns the ambiguity scanners leave behind into one evidence-backed
    disclosure.

    [:octicons-arrow-right-24: github.com/KjellKod/RepoLens](https://github.com/KjellKod/RepoLens)

-   :material-account-group:{ .lg .middle } __Quest__

    ---

    AI teamwork / multi-agent orchestration — plan, review, build, and fix features
    through coordinated agent handoffs with layered, independent verification.

    [:octicons-arrow-right-24: github.com/KjellKod/quest](https://github.com/KjellKod/quest)

-   :material-file-document-arrow-right:{ .lg .middle } __doc2md__

    ---

    Drop in a PDF, Word doc, spreadsheet, or slide deck and get clean Markdown
    back — converted entirely in your browser, so the files never leave your
    machine. It turns the documents you already have into context a coding agent
    can actually read.

    [:octicons-arrow-right-24: Try it live](https://kjellkod.github.io/doc2md/) ·
    [Source](https://github.com/KjellKod/doc2md)

-   :material-draw:{ .lg .middle } __sketch2md__

    ---

    An ASCII wireframe editor for agent-first development. Draw a UI, copy it as
    a Markdown code block, paste it into Claude Code, Codex, or Cursor — the agent
    gets layout, hierarchy, and structure with no guessing. The sketch sibling of
    doc2md.

    [:octicons-arrow-right-24: github.com/KjellKod/sketch2md](https://github.com/KjellKod/sketch2md)

</div>

## Battle-tested modern C++

Production-grade C++ libraries that have run in defense, financial,
medical-technology, and university systems — domains where "mostly works" was
never an option.

<div class="grid cards" markdown>

-   :material-math-log:{ .lg .middle } __g3log__

    ---

    Asynchronous, crash-safe C++ logger — 900+ stars and a decade of production
    use. Keeps logging right up to the moment of a crash, then flushes safely.

    [:octicons-arrow-right-24: github.com/KjellKod/g3log](https://github.com/KjellKod/g3log)

-   :material-connection:{ .lg .middle } __g3sinks__

    ---

    Sink integrations for g3log — rotating files, log levels, and more.

    [:octicons-arrow-right-24: github.com/KjellKod/g3sinks](https://github.com/KjellKod/g3sinks)

-   :material-sync:{ .lg .middle } __concurrent__

    ---

    Async FIFO wrapper that turns any C++ object into a background worker — simple,
    safe concurrency without the lock-juggling.

    [:octicons-arrow-right-24: github.com/KjellKod/concurrent](https://github.com/KjellKod/concurrent)

-   :material-rotate-360:{ .lg .middle } __lock-free-wait-free-circularfifo__

    ---

    A lock-free / wait-free circular FIFO — the classic single-producer,
    single-consumer concurrent data structure, done right.

    [:octicons-arrow-right-24: github.com/KjellKod/lock-free-wait-free-circularfifo](https://github.com/KjellKod/lock-free-wait-free-circularfifo)

</div>

## For engineering leaders

For CTOs, VPs of Engineering, and managers: before you sign a five-figure
contract with Jellyfish, LinearB, or Swarmia, start here. Open-source metrics
analysis that turns your team's own Jira and GitHub data into actionable insight
— so you understand more and coach better. Built to start conversations, not to
stack-rank people.

<div class="grid cards" markdown>

-   :material-chart-line:{ .lg .middle } __metrics-and-insights__

    ---

    Cycle time, release frequency, review latency, and the product-vs-platform
    balance — pulled straight from Jira and GitHub, exportable to CSV, and designed
    to spark better conversations with your team. Own your data; skip the expensive
    dashboard.

    [:octicons-arrow-right-24: github.com/KjellKod/metrics-and-insights](https://github.com/KjellKod/metrics-and-insights)

</div>
