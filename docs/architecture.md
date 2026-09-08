# Architecture

```mermaid
flowchart LR
    N0["Web / CLI"] --> N1
    N1["Case Service"] --> N2
    N2["Risk Rules"] --> N3
    N3["Relational Store"]
```

All data is synthetic and safe for public demonstration.
