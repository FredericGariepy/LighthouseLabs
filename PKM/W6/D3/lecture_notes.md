TRAFFIC LIGHT PROTOCOL (TLP)
https://www.first.org/tlp/

Resume Rubric
https://docs.google.com/document/d/1Sb2-6LsSSJo2_Zo46zaSw1aEZxoxcvKLgps7HbluJUo/edit

Flowchart automation: Use Mermaid files


https://app.diagrams.net/ \
Arrange > Insert > Advanced > Mermaid \
mermaid files automatically generate in github .md ! \
Open the code to see the mermaid script \
[Mermaid Docs](https://mermaid.js.org/intro/getting-started.html) \
fill:#ccf: This sets the background color of nodes.
stroke:#333: This sets the border color.
stroke-width:2px: This sets the border thickness.

```mermaid
graph TD
    A[Green ] --> B(Preview)
    B --> C{decide}
    C --> D[Keep]
    C --> E[Edit Definition]
    E --> B
    D --> F[Save Image and Code]
    F --> B

  classDef classA fill:#58eb34,stroke-width:0px
  classDef classB fill:#ccf,stroke:#333,stroke-width:2px;
  classDef classC fill:#cfc,stroke:#333,stroke-width:2px

  class A classA;
  class B classB;
  class D,F classC;
```

