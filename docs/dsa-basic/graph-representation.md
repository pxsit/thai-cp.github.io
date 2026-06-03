---
title: Graph Representaion
author: Thanabadee Thara-ngoen (Mingyuanz)
level:
---

กราฟสามารถ implement ได้ 3 แบบหลักๆด้วยกัน ได้แก่ Edge List, Adjacency Matrix, Adjacency List

## Edge List
* เก็บกราฟใน `vector<pair<int, int>> graph(m)` โดย m คือจำนวน edge ของกราฟ
* `graph[i]` เป็น `pair<int, int>` ที่เก็บ edge ที่ `i` ของกราฟ  
  โดยเก็บเป็น `{เลข vertex ด้านหนึ่งของ edge, เลข vertex อีกด้านของ edge}`

> Example: Unweighted Graph

กราฟในภาพดังกล่าวสามารถ represent ได้เป็น { {0,1}, {0,2}, {0,3}, {1,2}, {1,4}, {2,4}, {2,5}, {3,5} }
<img src="https://github.com/Mingyuanz1111/Algorithm-and-Data-Structure/assets/174484621/23b1a03b-8242-45fb-a74f-00d105310e94" width="800">

* ถ้าจะเก็บ weighted graph ให้ ใช้เป็น `vector<pair<pair<int, int>, int>>` (หรือ tuple ก็ได้ แล้วแต่ถนัด)
  ซึ่ง pair เก็บ `{{เลข vertex ด้านหนึ่งของ edge, เลข vertex อีกด้านของ edge}, weight ของ edge นั้น}`

> Example: Weighted Graph

กราฟในภาพดังกล่าวสามารถ represent ได้เป็น { {{0,1},4}, {{0,2},2}, {{0,3},3}, {{1,2},1}, {{1,4},3}, {{2,4},5}, {{2,5},3}, {{3,5},6} }
<img src="https://github.com/Mingyuanz1111/Algorithm-and-Data-Structure/assets/174484621/f675e4b4-4f79-4909-a81e-7a9434a6e4b5" width="800">

* สําหรับ edge List ถ้าเก็บ directed graph จําเป็นต้องสนใจลำดับของ vertex ใน pair ด้วย

## Adjacency Matrix
* ถ้าจะเก็บ weighted graph เก็บกราฟใน `int graph[n][n]` โดยที่ `n` คือจำนวน vertex ของกราฟ
  * `graph[i][j]` (row `i`, column `j`) แสดงถึง edge จาก vertex `i` ไป vertex `j` โดยค่าที่เก็บไว้จะเป็น weight ของ edge นั้น
* ถ้าไม่มี edge จาก `i` ไป `j` ให้ใส่ค่า `INF` ซึ่งในที่นี้ถูก define ไว้เป็นค่าที่สูงมากๆ ซึ่งความหมายเหมือนมี edge แต่ weight สูงมากๆจนข้ามไม่ได้ (บางครั้งอาจจะใส่ค่า `0` แล้วแต่ถนัด)

> Example:
<img src="https://github.com/Mingyuanz1111/Algorithm-and-Data-Structure/assets/174484621/8ad1554f-a053-4f2f-a1b4-17093c01bea6" width="800">

* ถ้าจะเก็บ unweighted Graph ให้ใส่ค่าเป็น 1 เมื่อมี edge และใส่ 0 ถ้าไม่มี edge (ใช้ `bool` เพื่อใช้ค่า true กับ false แทนได้เหมือนกัน)
* เมื่อเก็บ undirected graph จะต้องเพิ่ม edge หนึ่งใน 2 ทิศทางเสมอ ดังนั้น undirected graph จะมี adjacency matrix ที่สมมาตรเสมอ

## Adjacency List
* เก็บกราฟใน `vector<int> graph[n]` โดยที่ `n` เป็นจำนวน vertex
* `graph[i]` เป็น vector<int> ที่เก็บข้อมูลของ edge ทั้งหมดที่ชี้ออกจาก vertex `i` โดยเก็บเป็น เลข vertex ที่แต่ละ edge ชี้ไปหา

> Example: Unweighted Graph
<img src="https://github.com/Mingyuanz1111/Algorithm-and-Data-Structure/assets/174484621/946f5f8e-09a3-4511-9a34-b3417e8ee259" width="800">

* ถ้าจะเก็บ weighted graph ให้ใช้เป็น `vector<pair<int, int>>` แทน ซึ่งแต่ละ pair เก็บ `{เลข vertex ที่ไปหา, weight ของ edge นั้น}`

> Example: Weighted Graph
<img src="https://github.com/Mingyuanz1111/Algorithm-and-Data-Structure/assets/174484621/64270f22-1c7f-4a73-aff8-12e253a3aef2" width="800">

* ถ้าจะเก็บ Undirected Graph ให้ใส่ edge เดียวกันไปทั้ง 2 ด้าน  
  เช่น ตอนจะเพิ่ม edge ที่เชื่อม `a` กับ `b` ให้ทำทั้ง `graph[a].push_back(b), graph[b].push_back(a);`

