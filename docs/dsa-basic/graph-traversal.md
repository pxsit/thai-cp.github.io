---
title: Graph Traversal
author: Thanabadee Thara-ngoen (Mingyuanz)
level:
---

การสำรวจกราฟ หรือการท่องกราฟ คือการ"เยี่ยม"ทุกๆ vertex ของกราฟตามลำดับการสำรวจ โดยมักจะเริ่มจาก vertex เริ่มต้นบางจุดแล้วสำรวจ vertex ที่อยู่ติดกันไปเรื่อยๆจนกว่าจะครบทุก vertex

การสำรวจกราฟมีอยู่ 2 Algorithm หลักๆ ได้แก่ การค้นหาตามแนวลึก (Depth First Search, DFS), การค้นหาตามแนวกว้าง (Breadth First Search, BFS)
ซึ่งต่างก็มีสมบัติและประโยชน์ที่แตกต่างกัน

## การค้นหาตามแนวลึก (Depth First Search, DFS)

* เป็นการสำรวจกราฟที่มีแนวคิดโดยเริ่มต้นจาก vertex หนึ่งและสำรวจพุ่งลึกไปใน graph เรื่อยๆ จนกว่าจะตัน
  แล้วจึง backtrack ย้อนกลับมา vertex ก่อนหน้านี้ และสำรวจต่อไปเรื่อยๆไปยัง vertex ที่ยังไม่ถูกเยี่ยม จนกว่าจะเยี่ยมครบทุก vertex

### DFS โดยการเขียน Recursive Function

* วิธี implement ที่ง่ายที่สุด คือการเขียนฟังก์ชัน recursive เพื่อเรียกใช้จาก vertex เริ่มต้นอันหนึ่ง แล้ว recursive ไปหา vertex อื่นๆต่อเรื่อยๆ

> Code: ตัวอย่างการนำเข้าข้อมูลของกราฟ และสำรวจโดยใช้ DFS เริ่มจาก vertex ที่ 0

```c++
#define MAXN 200001
vector<int> graph[MAXN]; // adjacency list ของกราฟที่จะสำรวจ
bool visited[MAXN]; // มีค่าเป็น false ทุกช่อง

void dfs(int cur){ // ฟังก์ชัน DFS ที่เรียกเพื่อเยี่ยม vertex ที่ cur

    // จดว่า cur ถูกเยี่ยมแล้ว
    visited[cur] = true;

    // loop ทุก vertex รอบๆ cur ที่ยังไม่เคยถูกเยี่ยม เพื่อ recursive ไปเยี่ยมต่อ
    for(auto v: graph[cur]) 
        if(!visited[v]) 
            dfs(v);
}

int main(){
    // นำเข้าข้อมูลของกราฟ
    int n, m, u, v;
    cin >> n >> m; // กราฟมี n vertices, m edges
    for(int i=0; i<m; i++){
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    // กำหนด vertex เริ่มต้นการสำรวจ
    int src = 0;

    // เรียกฟังก์ชัน DFS เพื่อเริ่มสำรวจจากจุดเริ่มต้น
    dfs(src);

    return 0;
}
```

Time Complexity : $\mathcal{O}(n + m)$

* ในที่นี้จะใช้ adjacency list เพื่อเก็บโครงสร้างกราฟ และมี array `visited` เป็น array ที่เก็บค่า boolean ว่าแต่ละ vertex ถูกเยี่ยมไปแล้วหรือยัง ซึ่ง `visited[i]` จะมีค่าเป็น `true` เมื่อ vertex ที่ `i` เคย**ถูกเรียกฟังก์ชันไปหาแล้ว**
* ขั้นตอนแรกของ algorithm คือต้องกำหนด vertex เริ่มต้นใดก็ได้ แล้วเริ่มเรียกใช้ฟังก์ชันจาก vertex เริ่มต้นนั้น
เมื่อฟังก์ชันสำรวจไปถึง vertex หนึ่ง (พารามิเตอร์ `cur` ของฟังก์ชัน) ในฟังก์ชันจะทำขั้นตอนเรียงตามนี้

    1) **จดไว้ว่า vertex `cur` (vertex ปัจจุบัน) ถูกเยี่ยมไปแล้วทันที**

    2) เรียก recursive แต่ละ vertex รอบๆ cur ที่ยังไม่เคยถูกเยี่ยม

* เมื่อเยี่ยม vertex หนึ่ง หากไม่มี vertex รอบๆเลย หรือทุก vertex รอบๆถูกเยี่ยมหมดแล้ว จะไม่มีการ recursive ต่อ

* เมื่อฟังก์ชันนี้ถูกเรียก recursive ไปเรื่อยๆ จะมี vertex ในกราฟที่ถูกเยี่ยมมากขึ้นเรื่อยๆ จนสุดท้าย ฟังก์ชันจะทำงานเสร็จเมื่อทุก vertex ที่ไปหาได้จากจุดเริ่มต้นนั้นถูกเยี่ยมหมดแล้ว
* สังเกตว่าเมื่อจด vertex ปัจจุบันว่า visited ไว้ก่อนที่จะสำรวจต่อไป ทำให้ระหว่างสำรวจต่อ จะไม่มีการ recursive วนกลับมาที่ vertex เดิมซ้ำอีกแล้ว

* DFS สามารถ ทำให้ graph ใดๆ เป็น rooted tree ตามทางที่ search ไปได้ด้วย และ tree นั้นเรียกว่า DFS tree

> Example: DFS บน Graph ทั่วไป
<img src="../../assets/graph-traversal/dfs-recursive.jpg" alt = "" width="800">

### DFS บน tree โดยการเขียน Recursive Function

* ถ้า DFS บน tree ไม่จําเป็นต้องเก็บค่า visited ใน array ก็ได้ แต่ recursive โดยส่งต่อเลข vertex ของ parent แทน  
  เพราะ tree ไม่มี cycle ดังนั้นเมื่อสำรวจไปถึง vertex หนึ่ง จะการันตีได้ว่ามีแค่ node parent ที่เคยเยี่ยมไปแล้ว ขั้นตอน recursive จึงเรียกฟังก์ชันต่อทุก vertex ข้างๆมัน ยกเว้น parent ของมัน

> Code: ตัวอย่างการนำเข้าข้อมูลของกราฟต้นไม้ และสำรวจโดยใช้ DFS เริ่มจาก vertex ที่ 0

```c++
#define MAXN 200001
vector<int> graph[MAXN]; // adjacency list ของกราฟต้นไม้ที่จะสำรวจ
void dfs(int cur, int prev){  // ฟังก์ชัน DFS ที่เรียกเพื่อเยี่ยม vertex ที่ cur โดย vertex ก่อนหน้านี้คือ prev

    // loop ทุก vertex รอบๆ cur ยกเว้น prev เพื่อ recursive ไปเยี่ยมต่อ
    for(auto v : graph[cur]) 
        if(v != prev) 
            dfs(v, cur);
}

int main(){
    // นำเข้าข้อมูลของกราฟต้นไม้
    int n, m, u, v;
    cin >> n >> m; // กราฟมี n vertices, m edges
    for(int i=0; i<n-1; i++){
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    // กำหนด vertex เริ่มต้นการสำรวจ ซึ่งมองว่าเป็น root ของ tree ก็ได้
    int src = 0;

    // เรียกฟังก์ชัน DFS เพื่อเริ่มสำรวจจากจุดเริ่มต้น
    dfs(src, src); // ให้พารามิเตอร์ prv มีค่าเป็น src ก็ได้ เพราะไม่มี vertex ก่อนหน้ามันเลย

    return 0;
}
```

Time Complexity : $\mathcal{O}(n + m)$

> Example: DFS บน Tree
<img src="../../assets/graph-traversal/dfs-recursive-tree.jpg" alt="" width="800">

### DFS โดยใช้ Stack

* วิธี implement คือการใช้โครงสร้างข้อมูล stack มาช่วยในการจัดลำดับการสำรวจ เนื่องจากโครงสร้างนี้มีลำดับการสำรวจเหมือนกับการ recursive โดย stack นี้จะเก็บลำดับของ vertex ที่**รอทำการสำรวจ**อยู่

* เมื่อต้องการสำรวจ vertex ต่อไป ให้สำรวจ vertex ที่อยู่ด้านบนสุดของ stack ก่อน แล้ว pop มันออก และเมื่อเจอ vertex รอบๆมันที่ยังไม่เคยเจอ ให้ push เข้า stack เพื่อรอสำรวจต่อไป

* วิธีนี้อาจไม่สะดวกต่อการเขียนเท่าการ recursive แต่วิธีนี้มักใช้แทนการ recursive ตอนที่ใช้ recursive แล้ว memory limit exceeded แต่โจทย์ส่วนใหญ่ให้ memory เพียงพอสำหรับการ recursive อยู่แล้ว

> Code: ตัวอย่างการนำเข้าข้อมูลของกราฟ และสำรวจโดยใช้ DFS เริ่มจาก vertex ที่ 0 โดยใช้ stack

```c++
#define MAXN 200001
vector<int> graph[MAXN]; // adjacency list ของกราฟที่จะสำรวจ
bool visited[MAXN]; // มีค่าเป็น false ทุกช่อง

int main(){
    // นำเข้าข้อมูลของกราฟ
    int n, m, u, v;
    cin >> n >> m; // กราฟมี n vertices, m edges
    for(int i=0; i<m; i++){
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    // กำหนด vertex เริ่มต้นการสำรวจ
    int src = 0;

    // เริ่มทำการ DFS
    stack<int> st;
    st.push(src); // นำ vertex เริ่มต้น push ใส่ใน stack

    while(!st.empty()){

        // นำเลข vertex ที่อยู่บนสุดของ stack มาใส่ตัวแปร cur และ pop มันออก
        int cur = st.top();
        st.pop();

        // ถ้า cur ถูกเยี่ยมแล้ว ให้ข้ามทันที
        if(visited[cur]) continue;

        // จดว่า cur ถูกเยี่ยมแล้ว
        visited[cur] = true;

        // loop ทุก vertex รอบๆ cur ที่ยังไม่ถูกเยี่ยมแล้วทำการเพิ่มใส่ stack ต่อ
        for(auto v: graph[cur]) 
            if(!visited[v])
                st.push(v);
        
    }

    return 0;
}
```

Time Complexity : $\mathcal{O}(n + m)$

* ในที่นี้จะใช้ adjacency list เพื่อเก็บโครงสร้างกราฟ และมี array `visited` เป็น array ที่เก็บค่า boolean ว่าแต่ละ vertex ถูกเยี่ยมไปแล้วหรือยัง ซึ่ง `visited[i]` จะมีค่าเป็น `true` เมื่อ vertex ที่ `i` เคย**ถูก pop ออกจาก stack และสำรวจไปแล้ว**
* ขั้นตอนแรกของ algorithm คือต้องกำหนด vertex เริ่มต้นใดก็ได้ แล้วนำเลข vertex เริ่มต้นนั้นไป push ใส่ stack

* หลังจากนั้นจะใช้ while loop เพื่อทำขั้นตอนเรียงตามนี้ในการ loop แต่ละครั้ง :

    1) นำเลข vertex ที่อยู่บนสุดของ stack มาใส่ตัวแปร `cur` เพื่อความง่ายต่อการใช้งาน

    2) pop เลข vertex ที่อยู่บนสุดของ stack ออก เนื่องจากกำลังจะสำรวจ vertex นี้แล้ว

    3) ถ้า vertex `cur` นั้นถูกเยี่ยมแล้ว ให้ข้ามไปเริ่มการ loop ครั้งต่อไปทันที

    4) จด vertex `cur` ว่าถูกเยี่ยมไปแล้ว

    5) push แต่ละ vertex ที่อยู่ติดกับ `cur` และยังไม่เคยถูกเยี่ยม เข้าไปใน stack เพื่อรอทำการเยี่ยมใน loop ครั้งต่อๆไป

* loop จะจบลงเมื่อ stack ว่าง เพราะมันหมายความว่าไม่มี vertex ใดให้สำรวจต่อแล้ว
* เมื่อมีการ loop ต่อไปเรื่อยๆ จะมี vertex ในกราฟที่ถูกเยี่ยมมากขึ้นเรื่อยๆ จนสุดท้าย loop จะทำงานเสร็จเมื่อทุก vertex ที่ไปหาได้จากจุดเริ่มต้นนั้นถูกเยี่ยมหมดแล้ว
* สังเกตว่าเมื่อจด vertex ปัจจุบันว่า visited ไว้ก่อนที่จะสำรวจต่อไป ทำให้ระหว่างสำรวจต่อ จะไม่มีการสำรวจจาก vertex เดิมซ้ำอีกแล้ว

### DFS บนกราฟที่ไม่เชื่อมต่อกันทั้งหมด

* สำหรับกราฟที่ไม่เชื่อมต่อกันทั้งหมด การสำรวจโดยเริ่มจาก vertex เริ่มต้นเพียงจุดเดียวอาจสำรวจได้ไม่ครบทั้งกราฟ เพราะอาจมีบาง vertex ที่เข้าถึงจากจุดเริ่มต้นไม่ได้
ดังนั้น กรณีต้องการ DFS สำรวจทุก vertex ในกราฟประเภทดังกล่าว ต้องทำการ loop ทุกๆ vertex เริ่มต้นที่เป็นไปได้ และตรวจสอบว่า vertex นั้นถูกเยี่ยมโดยการ DFS ครั้งก่อนๆไปแล้วหรือยัง ถ้ายังไม่ถูกเยี่ยมก็ให้ทำการ DFS เริ่มจาก vertex นั้นเลย

> Code: ตัวอย่างการสำรวจกราฟที่ไม่เชื่อมต่อกันทั้งหมด โดยใช้ DFS

```c++
for(int src=0; src<n; src++) {
    // หากสำรวจ vertex นั้นไปแล้วให้ข้าม
    if(visited[src]) continue;

    // เริ่มทำการ DFS โดยเริ่มจาก vertex ที่ src
    dfs(src);  
}
```

Time Complexity : $\mathcal{O}(n + m)$

## การค้นหาตามแนวกว้าง (Breadth First Search, BFS)

* เป็นการสำรวจกราฟโดยเริ่มต้นจาก vertex หนึ่ง และสำรวจ vertex อื่นๆเป็นแนวกว้างออกจาก vertex เริ่มต้น ทีละความลึกของกราฟนับจาก vertex เริ่มต้นไปเรื่อยๆ จนกว่าจะเยี่ยมครบหมดทุก vertex

(คำว่า "ความลึก" ในที่นี้หมายถึง ระยะทางที่สั้นที่สุดในการเดินทางผ่าน edge ต่างๆเริ่มจาก vertex เริ่มต้น)

### BFS โดยใช้ Queue

* วิธี implement BFS จะมีวิธีเหมือนกับการ implement DFS โดยใช้ stack เพียงแค่เปลี่ยนจากการใช้ stack มาใช้ queue แทน

* วิธี implement คือการใช้โครงสร้างข้อมูล queue มาช่วยในการจัดลำดับการสำรวจ โดย queue นี้จะเก็บลำดับของ vertex ที่**รอทำการสำรวจ**อยู่

* เมื่อต้องการสำรวจ vertex ต่อไป ให้สำรวจ vertex ที่อยู่ด้านหน้าสุดของ queue ก่อน แล้ว pop มันออก และเมื่อเจอ vertex รอบๆมันที่ยังไม่เคยเจอ ให้ push เข้า queue เพื่อรอสำรวจต่อไป

* ที่ทำเช่นนี้แล้วสามารถสำรวจทีละความลึกของกราฟได้ เพราะว่า หากเราพิจารณา vertex ใน queue เพียงแค่ตัวที่ยังไม่เคยถูก visit จะได้ว่า
    * ตอนเริ่มแรก queue มีเพียงแค่ vertex ที่ความลึกเท่ากับ 0 ซึ่งก็คือ vertex เริ่มต้น
    * หลังจากที่เยี่ยม vertex เหล่านั้นเสร็จ ใน queue จะมีเพียง vertex ที่ความลึกเท่ากับ 1
    * หลังจากที่เยี่ยม vertex เหล่านั้นเสร็จ ใน queue จะมีเพียง vertex ที่ความลึกเท่ากับ 2
เป็นเช่นนี้ไปเรื่อยๆนั่นเอง

> Code: ตัวอย่างการนำเข้าข้อมูลของกราฟ และสำรวจโดยใช้ BFS เริ่มจาก vertex ที่ 0 โดยใช้ queue

```c++
#define MAXN 200001
vector<int> graph[MAXN]; // adjacency list ของกราฟที่จะสำรวจ
bool visited[MAXN]; // มีค่าเป็น false ทุกช่อง

int main(){
    // นำเข้าข้อมูลของกราฟ
    int n, m, u, v;
    cin >> n >> m; // กราฟมี n vertices, m edges
    for(int i=0; i<m; i++){
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    // กำหนด vertex เริ่มต้นการสำรวจ
    int src = 0;

    // เริ่มทำการ BFS
    queue<int> que;
    que.push(src); // นำ vertex เริ่มต้น push ใส่ใน queue

    while(!que.empty()){

        // นำเลข vertex ที่อยู่หน้าสุดของ queue มาใส่ตัวแปร cur และ pop มันออก
        int cur = que.front();
        que.pop();

        // ถ้า cur ถูกเยี่ยมแล้ว ให้ข้ามทันที
        if(visited[cur]) continue;

        // จดว่า cur ถูกเยี่ยมแล้ว
        visited[cur] = true;

        // loop ทุก vertex รอบๆ cur ที่ยังไม่ถูกเยี่ยมแล้วทำการเพิ่มใส่ queue ต่อ
        for(auto v: graph[cur]) 
            if(!visited[v])
                que.push(v);

    }

    return 0;
}
```

Time Complexity : $\mathcal{O}(n + m)$

* ในที่นี้จะใช้ adjacency list เพื่อเก็บโครงสร้างกราฟ และมี array `visited` เป็น array ที่เก็บค่า boolean ว่าแต่ละ vertex ถูกเยี่ยมไปแล้วหรือยัง ซึ่ง `visited[i]` จะมีค่าเป็น `true` เมื่อ vertex ที่ `i` เคย**ถูก pop ออกจาก queue และสำรวจไปแล้ว**
* ขั้นตอนแรกของ algorithm คือต้องกำหนด vertex เริ่มต้นใดก็ได้ แล้วนำเลข vertex เริ่มต้นนั้นไป push ใส่ queue

* หลังจากนั้นจะใช้ while loop เพื่อทำขั้นตอนเรียงตามนี้ในการ loop แต่ละครั้ง :

    1) นำเลข vertex ที่อยู่ด้านหน้าสุดของ queue มาใส่ตัวแปร `cur` เพื่อความง่ายต่อการใช้งาน

    2) pop เลข vertex ที่อยู่ด้านหน้าสุดของ queue ออก เนื่องจากกำลังจะสำรวจ vertex นี้แล้ว

    3) ถ้า vertex `cur` นั้นถูกเยี่ยมแล้ว ให้ข้ามไปเริ่มการ loop ครั้งต่อไปทันที

    4) จด vertex `cur` ว่าถูกเยี่ยมไปแล้ว

    5) push แต่ละ vertex ที่อยู่ติดกับ `cur` และยังไม่เคยถูกเยี่ยม เข้าไปใน queue เพื่อรอทำการเยี่ยมใน loop ครั้งต่อๆไป

* loop จะจบลงเมื่อ queue ว่าง เพราะมันหมายความว่าไม่มี vertex ใดให้สำรวจต่อแล้ว
* เมื่อมีการ loop ต่อไปเรื่อยๆ จะมี vertex ในกราฟที่ถูกเยี่ยมมากขึ้นเรื่อยๆ จนสุดท้าย loop จะทำงานเสร็จเมื่อทุก vertex ที่ไปหาได้จากจุดเริ่มต้นนั้นถูกเยี่ยมหมดแล้ว
* สังเกตว่าเมื่อจด vertex ปัจจุบันว่า visited ไว้ก่อนที่จะสำรวจต่อไป ทำให้ระหว่างสำรวจต่อ จะไม่มีการสำรวจจาก vertex เดิมซ้ำอีกแล้ว

* BFS สามารถ ทำให้ graph ใดๆ เป็น Rooted Tree ตามทางที่ search ไปได้ด้วย Tree นั้นเรียกว่า BFS Tree

> Example: BFS บน Graph ทั่วไป
<img src="../../assets/graph-traversal/bfs-queue.jpg" alt="" width="800">

### BFS บนกราฟที่ไม่เชื่อมต่อกันทั้งหมด

* สำหรับกราฟที่ไม่เชื่อมต่อกันทั้งหมด การสำรวจโดยเริ่มจาก vertex เริ่มต้นเพียงจุดเดียวอาจสำรวจได้ไม่ครบทั้งกราฟ เพราะอาจมีบาง vertex ที่เข้าถึงจากจุดเริ่มต้นไม่ได้
ดังนั้น กรณีต้องการ BFS สำรวจทุก vertex ในกราฟประเภทดังกล่าว ต้องทำการ loop ทุกๆ vertex เริ่มต้นที่เป็นไปได้ และตรวจสอบว่า vertex นั้นถูกเยี่ยม (ถูก push ใส่ queue) โดยการ BFS ครั้งก่อนๆไปแล้วหรือยัง ถ้ายังไม่ถูกเยี่ยมก็ให้ทำการ BFS เริ่มจาก vertex นั้นเลย

> Code: ตัวอย่างการสำรวจกราฟที่ไม่เชื่อมต่อกันทั้งหมด โดยใช้ BFS

```c++
for(int src=0; src<n; src++){
    // หากสำรวจ vertex นั้นไปแล้วให้ข้าม
    if(visited[src]) continue;

    // เริ่มทำการ BFS โดยเริ่มจาก vertex ที่ src
    queue<int> que;
    que.push(src);

    while(!que.empty()){
        int cur = que.front();
        que.pop();

        if(visited[cur]) continue;

        visited[cur] = true;

        for(auto v: graph[cur])
            if(!visited[v])
                que.push(v);
        
    }
}
```

Time Complexity : $\mathcal{O}(n + m)$

## โจทย์

!unfinished
