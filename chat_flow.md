```mermaid
---
title: Reflection chat
---

sequenceDiagram
autonumber

actor user as User
participant io as I/O
participant log as Logic
participant ai as AI
participant storage as Storage

io-->>user:start of chat
user->>io:response to chatbot

```