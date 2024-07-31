TRAFFIC LIGHT PROTOCOL (TLP)
https://www.first.org/tlp/

SLA : trigger points for escalations.






Resume Rubric
https://docs.google.com/document/d/1Sb2-6LsSSJo2_Zo46zaSw1aEZxoxcvKLgps7HbluJUo/edit

Flowchart automation: Use Mermaid files

https://app.diagrams.net/ \
Arrange > Insert > Advanced > Mermaid \
mermaid files automatically generate in github .md ! \
Open the code to see the mermaid script \
[Mermaid Docs](https://mermaid.js.org/intro/getting-started.html)
- fill:#ccf: This sets the background color of nodes, Hex.
- stroke:#333: This sets the border color, Hex.
- stroke-width:2px: This sets the border thickness, Pixel.
- TD : top down , LR: left to right 
```mermaid
graph LR
    A[Green square no border] --> B(Blue rounded border)
    B --> C{Diamond default style}
    C --> D[square default style]
    C --> E[White square no border]
    E --> B
    D --> F[White square no border]
    F --> B

  classDef classA fill:#58eb34,stroke-width:0px
  classDef classB fill:#ffffff,stroke:#75aaff,stroke-width:2px;
  classDef classC fill:#ffffff,stroke:#ffffff,stroke-width:0px

  class A classA;
  class B classB;
  class F,E classC;
```
```mermaid 
flowchart TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Result 1]
    B -->|No| D[Result 2]
    C --> E[End]
    D --> E[End]
```

