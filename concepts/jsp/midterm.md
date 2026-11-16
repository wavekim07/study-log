# 웹프로그래밍(JSP) 중간고사 쉬운 정리

> **시험** 10/20(화) 15:30 · 수업하던 강의실 (자리는 한 칸씩 띄워 앉기) · 10/21(수) 수업 없음
> **범위** 이번 주 마지막 수업까지 (교수님이 "목요일, 아니 내일"로 정정 → 날짜는 공지 확인)
> **형태** 수업 예제 중심. 설명하는 문제 + **코드를 직접 쓰는** 문제
> **안 나오는 것** HTML, CSS. **나오는 것** JSP와 관련된 내용만

**이 문서 읽는 법**
각 장은 이 순서예요: 비유(쉬운 그림) → 개념 → 코드 → 외울 것 → 자주 하는 실수.
코드는 눈으로만 보지 말고, 장마다 **백지에 직접 써보세요.** 시험이 "쓰는 문제"라서요.

**교수님이 짚은 순서 = 이 문서의 순서**

| 장 | 내용 | 시험에서 |
|---|---|---|
| 1 | 웹 구조와 JSP 동작 원리 | 설명하는 문제 |
| 2 | 스크립트 태그 (3종 + page) | 코드, 설명 |
| 3 | 액션 태그 (include, forward) | 코드, 설명 |
| 4 | request, session 객체 (로그인) | 코드, 설명 |
| 5 | 데이터베이스와 MySQL 기본 | 설명 |
| 6 | SQL (insert, select, update, delete) | 코드를 쓰는 문제 |
| 7 | DAO, DTO 만들기 (오늘 수업) | 코드, 설명 |
| 8 | 백지 연습문제 + 정답 | 최종 점검 |

---

## 1장. 웹 구조와 JSP 동작 원리

### 1-1. 웹은 "주문하고 받는" 구조예요

**비유**: 식당이에요.

- **손님 = 클라이언트(브라우저)**: 주문(요청, request)을 해요.
- **주방 = 웹 서버(Tomcat)**: 요리해서 음식(응답, response)을 내줘요.
- 손님은 주방 안을 못 봐요. 완성된 음식(HTML)만 받아요.

| 용어 | 뜻 |
|---|---|
| 요청 (Request) | 브라우저가 서버에 "이 페이지 줘"라고 하는 것 |
| 응답 (Response) | 서버가 결과(HTML)를 돌려주는 것 |
| HTTP | 요청과 응답을 주고받는 약속(규칙) |
| Tomcat | JSP를 실행해주는 웹 서버 (웹 컨테이너) |

### 1-2. 왜 JSP를 쓰나요?

Java로 웹 페이지를 만들면 **서블릿(HttpServlet)** 이라는 클래스를 써요.
그런데 HTML을 전부 문자열로 출력해야 해서 너무 불편해요.

```java
out.print("<h1>Hello JSP</h1>");   // HTML을 Java 안에 문자열로 써야 함
```

그래서 반대로 했어요. **HTML 안에 Java를 끼워 넣는** 방식이 **JSP**예요.

- 서블릿: Java 안에 HTML을 넣음 (Java가 주인공)
- JSP: HTML 안에 Java를 넣음 (HTML이 주인공)

### 1-3. JSP가 실행되는 과정 (시험 핵심)

**비유**: 손님이 "test.jsp 주세요"라고 주문하면, 주방(Tomcat)이 **레시피(JSP)를 Java 요리책(서블릿)으로 번역**한 뒤 요리해서 내줘요.

```
브라우저: localhost:8080/HelloJSP/test.jsp 요청
        ↓
① Tomcat이 test.jsp를 찾음
        ↓ 변환
② test_jsp.java 생성 (서블릿 클래스: HttpServlet을 상속)
        ↓ 컴파일
③ test_jsp.class 생성
        ↓ JVM이 실행
④ 실행 결과 = HTML 문서
        ↓
브라우저가 HTML을 받아 화면에 표시
```

외울 한 줄: **JSP → 서블릿(.java) 변환 → 컴파일(.class) → JVM 실행 → HTML 응답**

**주소(URL) 읽는 법**: `localhost:8080/HelloJSP/test.jsp`

- `localhost:8080` : 내 컴퓨터의 Tomcat 서버 (8080은 포트 번호)
- `HelloJSP` : 프로젝트 이름
- `test.jsp` : 요청한 파일

### 1-4. 변환될 때 코드는 어디로 들어갈까요? (필기의 그림)

필기에 `int w,h` / `_jspService()` / `getSize()` 그림이 있죠? 이 뜻이에요.

```java
// test.jsp가 이렇게 바뀐다고 생각하면 돼요 (test_jsp.java)
public class test_jsp extends HttpServlet {

    int w, h;                       // ← 선언부 <%! %> 의 변수
    private int getSize() { ... }   // ← 선언부 <%! %> 의 함수

    public void _jspService(...) {  // ← 요청이 올 때마다 실행되는 메서드
        w = 7;                      // ← 스크립틀릿 <% %> 의 코드
        h = 11;
        int size = w * h;
    }
}
```

- `<%! %>` 안의 것은 **클래스의 멤버**(변수, 함수)가 돼요.
- `<% %>` 안의 것은 **`_jspService()` 메서드 안**에 들어가요.

> **헷갈리면 이렇게**: 선언부는 "클래스 밖 공용 도구", 스크립틀릿은 "요청받을 때마다 하는 일".

### 외울 것

- 웹 동작: 요청 → Tomcat → JSP를 서블릿으로 변환 → 컴파일 → 실행 → HTML 응답
- JSP는 "화면을 만들어 보여주는" 역할(Presentation)
- 서블릿 = Java 안에 HTML, JSP = HTML 안에 Java

### 자주 하는 실수

- 브라우저는 **JSP 코드를 볼 수 없어요.** 받는 건 실행이 끝난 HTML뿐이에요.
- JSP 파일은 더블클릭이 아니라 **서버(Tomcat)를 통해** 열어야 해요 (`localhost:8080/...`).

---

## 2장. 스크립트 태그

### 2-1. 비유: HTML 문서에 "Java 구멍" 뚫기

HTML 사이에 `<% %>` 모양으로 구멍을 내고, 그 안에만 Java를 써요. **태그 모양마다 역할이 달라요.**

| 태그 | 이름 | 하는 일 | 비유 |
|---|---|---|---|
| `<%! ... %>` | 선언 | 변수, 함수 **만들기** | 도구 준비 |
| `<% ... %>` | 스크립틀릿 | 연산, if, for, 함수 호출 등 **실행** | 요리하기 |
| `<%= ... %>` | 표현식 | 값을 화면에 **출력** | 접시에 담기 |
| `<%@ page ... %>` | 지시자 | 페이지 설정 (인코딩 등) | 주문서 머리말 |

### 2-2. 한 번에 보는 예제

```jsp
<%@ page contentType="text/html; charset=UTF-8" %>

<%! int w = 7, h = 11;
    int getSize() { return w * h; } %>

<html>
<body>
  <h1>사각형 넓이</h1>

  <% int size = getSize();
     if (size > 50) { %>
       <p>큰 사각형이에요.</p>
  <% } %>

  <p>가로 : <%= w %></p>
  <p>세로 : <%= h %></p>
  <p>넓이 : <%= size %></p>
</body>
</html>
```

- `<%= w %>` 는 `out.print(w);` 와 같아요. **세미콜론(;)을 안 붙여요.**
- `<% %>` 안에서 `{`를 열고 `%>`로 닫은 뒤, HTML을 쓰고, 다시 `<% } %>`로 닫을 수 있어요. (위 if문처럼)

### 2-3. 반복문과 함께 쓰기 (자주 나와요)

```jsp
<% for (int i = 1; i <= 5; i++) { %>
    <li><%= i %> 번째 줄</li>
<% } %>
```

### 2-4. 예제 ① 사칙연산 계산기 (form → request)

**흐름**: 입력 화면(calc.html) → 계산 버튼 → 계산 페이지(calc.jsp)

```jsp
<%-- calc.jsp --%>
<%
  int a = Integer.parseInt(request.getParameter("a"));
  int b = Integer.parseInt(request.getParameter("b"));
%>
<p>a + b = <%= a + b %></p>
<p>a - b = <%= a - b %></p>
<p>a * b = <%= a * b %></p>
<p>a / b = <%= a / b %></p>
```

- 입력창에 쓴 값은 `request.getParameter("이름")`으로 꺼내요.
- **꺼낸 값은 항상 문자열(String)** 이에요. 계산하려면 숫자로 바꿔요.
  - 정수: `Integer.parseInt(문자열)`
  - 실수: `Double.parseDouble(문자열)`
- 주소창에 `calc.jsp?a=4&b=5`처럼 값이 실려가요. 이걸 **Query String**이라고 해요.

### 2-5. 예제 ② 카페 메뉴 주문 (Java = 데이터·관리, JSP = 출력)

필기의 "Java : Data + Management, JSP : Presentation" 이 이 예제의 핵심 원칙이에요.

| 파일 | 역할 |
|---|---|
| `Menu.java` | 메뉴 하나(이름, 가격)를 담는 **데이터 클래스** |
| `MenuManager.java` | 메뉴 목록을 만들고 관리 (데이터 + 관리) |
| `menu.jsp` | 메뉴 목록과 주문 입력을 **보여주기** |
| `order.jsp` | 주문 목록, 합계 **출력** |
| `OrderItem.java` | 주문 한 줄(메뉴 + 수량) 데이터 클래스 |

**흐름**: `menu.jsp`에서 수량 입력 → form get 방식 → Query String(`?Amer=2&Latte=3&Tea=4`) → `order.jsp`가 받아서 주문 목록 출력

BMI 예제도 같은 생각이에요. 키와 몸무게로 `BMI = 몸무게 / 키²`를 계산하는 걸 **Java 클래스(Member: name, w, h, bmi)** 가 하고, JSP는 결과만 출력해요.

### 2-6. 왜 이렇게 나눌까요?

JSP에 계산, 데이터, 출력을 다 넣으면 코드가 엉켜서 알아보기 어려워요. 그래서 **계산·데이터는 Java 클래스**, **출력은 JSP**로 나눠요. 이 생각이 7장 DAO/DTO까지 이어져요.

### 외울 것

- `<%! %>` 선언 / `<% %>` 스크립틀릿 / `<%= %>` 표현식 / `<%@ page %>` 지시자
- 입력값 꺼내기: `request.getParameter("이름")` → 결과는 **String**
- 숫자 변환: `Integer.parseInt()`, `Double.parseDouble()`

### 자주 하는 실수

- `<%= x; %>` 처럼 세미콜론을 붙이면 오류가 나요.
- `<% %>` 와 `<%! %>` 를 바꿔 쓰는 것. 변수·함수 **정의**는 `<%! %>`, 그 외 **실행**은 `<% %>`.
- 문자열 `"4" + "5"`는 `"45"`예요. 숫자로 바꾸고 더해야 `9`예요.

---

## 3장. 액션 태그

### 3-1. 비유: 건물에 "다른 방 끼워 넣기, 다른 방으로 보내기"

스크립트 태그는 Java를 쓰는 구멍이었다면, **액션 태그는 JSP 페이지끼리 연결**해주는 태그예요. 모양은 `<jsp:이름 />` 이에요.

| 태그 | 하는 일 | 비유 |
|---|---|---|
| `<jsp:include>` | 다른 페이지를 **내 안에 포함** | 보고서에 그림 한 장 끼우기 |
| `<jsp:forward>` | 처리를 **다른 페이지로 넘김** | 전화를 다른 부서로 돌려주기 |

### 3-2. include (포함)

`A.jsp`를 요청했는데, A 안에서 `b.jsp`를 포함해요. 실행이 끝나면 **다시 A로 돌아와서** 나머지를 실행해요. (A ⇄ B)

```jsp
<%-- a.jsp --%>
<h1>A 페이지</h1>
<jsp:include page="b.jsp" />
<p>다시 A로 돌아와서 계속 출력</p>
```

**어디에 쓰나요? 레이아웃(모듈화)**: 모든 페이지에 똑같이 들어가는 부분(머리, 메뉴, 아래 정보)을 파일로 하나씩 만들어두고 가져다 써요. 필기의 Header / Menu / sidebar / Footer 그림이 이거예요.

```jsp
<jsp:include page="header.jsp" />
<jsp:include page="menu.jsp" />
  ... 이 페이지만의 내용 (main) ...
<jsp:include page="footer.jsp" />
```

> 머리·메뉴를 고치고 싶으면 파일 하나만 고치면 모든 페이지가 바뀌어요.

**include는 두 가지 방식이 있어요** (필기의 ① ②)

| | ① 액션 태그 | ② 지시자 |
|---|---|---|
| 모양 | `<jsp:include page="b.jsp" />` | `<%@ include file="b.jsp" %>` |
| 합치는 시점 | **실행할 때** 결과를 포함 | **변환할 때** 소스를 합침 |
| 비유 | 완성된 요리를 접시에 같이 담기 | 레시피 두 장을 한 장으로 합치기 |

### 3-3. forward (이동)

`A`에서 `B`로 **처리를 완전히 넘겨요.** 돌아오지 않아요. (A → B)

```jsp
<%-- index2.jsp --%>
<jsp:forward page="products.jsp" />
```

- 브라우저 주소창은 그대로 `index2.jsp`예요. (사용자는 넘어간 줄 몰라요)
- forward 할 때 **request 객체도 함께 넘어가요.** (4장에서 더 나와요)

### 3-4. include와 forward 비교 (자주 나오는 설명 문제)

| | include | forward |
|---|---|---|
| 흐름 | A ⇄ B (갔다가 **돌아옴**) | A → B (**안 돌아옴**) |
| 결과 화면 | A와 B가 합쳐진 한 페이지 | B만 보임 |
| 주 용도 | 공통 부분(머리, 메뉴, 푸터) 재사용 | 처리 후 다른 페이지로 이동 |

### 3-5. 예제: 상품 목록 → 상품 상세

필기의 `index2.jsp → products.jsp → product_detail.jsp` 흐름이에요.

1. `index2.jsp` : `<jsp:forward page="products.jsp" />` 로 목록으로 보냄
2. `products.jsp` : 상품 목록(`dataList`, `Product.java`로 만든 데이터)을 출력
3. 상품을 클릭 `<a href="product_detail.jsp?...">` : 선택한 상품의 상세 정보를 보여줌

### 3-6. useBean (form을 객체로)

form에 입력한 값들을 **자동으로 객체로 만들어주는** 액션 태그예요. (필기의 form → 객체 생성 `useBean`)

```jsp
<jsp:useBean id="user2" class="dto.User" />
<jsp:setProperty name="user2" property="*" />
```

- `useBean` = `User user2 = new User();` 를 대신 써주는 것
- `setProperty` = form 값을 `user2.setUid(...)` 처럼 객체에 담아주는 것
- 이 방식을 쓰는 데이터 클래스를 **JavaBean(자바빈즈)** 이라고 불러요. (private 변수 + getter/setter)

### 외울 것

- include = 포함하고 **돌아옴** / forward = 넘기고 **안 돌아옴**
- `<jsp:include page="..." />`, `<jsp:forward page="..." />`
- 지시자 include: `<%@ include file="..." %>`
- JavaBean = private 변수 + getter/setter가 있는 데이터 클래스

### 자주 하는 실수

- `<jsp:include page="b.jsp">` 처럼 끝의 `/`를 빼먹으면 태그가 안 닫혀서 오류가 나요.
- forward 뒤에 쓴 코드는 실행되지 않아요(이미 넘어갔으니까요).

---

## 4장. request, session 객체

### 4-1. 전달 객체(내장 객체) 4개

JSP에는 **선언하지 않아도 그냥 쓸 수 있는 객체**가 있어요. 그중 값을 전달·보관하는 4개를 **"살아있는 범위"** 로 구분해요. (필기 오른쪽 아래)

| 객체 | 범위 | 비유 |
|---|---|---|
| `page` | 그 페이지 안에서만 | 내 손에 든 메모 |
| `request` | 요청 한 번 (forward된 페이지까지) | 주문서 한 장 |
| `session` | 브라우저 하나, 접속 동안 | 내 이름이 적힌 사물함 |
| `application` | 서버가 켜져 있는 동안, 모두 공유 | 가게 입구 공용 게시판 |

### 4-2. 먼저, HTTP는 기억력이 없어요 (Stateless)

필기의 `HTTP Protocol = "Stateless"`예요.

**비유**: 가게 점원이 매번 나를 처음 보는 사람처럼 대해요. 방금 로그인했는데, 다음 페이지를 열면 "누구세요?" 하는 거예요.

- 페이지를 이동하면 request는 사라져요. (요청 한 번 = 한 번의 만남)
- 그래서 "이 사람은 로그인한 사람이야"를 **기억해둘 곳**이 필요해요. 그게 **session**이에요.

### 4-3. session은 어떻게 사람을 알아볼까요? (필기 그림)

**비유**: 놀이공원 **손목 밴드 + 사물함**이에요.

1. 브라우저가 처음 요청하면, 서버가 **세션 ID(SID)** 를 만들어요. (손목 밴드 번호)
2. 서버에 **session 객체**(사물함)를 만들고 그 ID와 연결해요.
3. 서버가 SID를 브라우저에 줘요. (브라우저가 SID를 기록)
4. 다음부터 브라우저는 **요청할 때마다 SID를 같이** 보내요.
5. 서버는 SID를 보고 "아, 사물함 17번 사람이네" 하고 내용을 꺼내요.

### 4-4. 객체별 메서드 (필기 오른쪽 위)

| 하는 일 | 코드 | 값의 종류 |
|---|---|---|
| 입력값(form) 꺼내기 | `request.getParameter("이름")` | **String** |
| 객체 저장 | `request.setAttribute("이름", 값)` | Object |
| 객체 꺼내기 | `request.getAttribute("이름")` | Object (형변환 필요) |
| session에 저장 | `session.setAttribute("이름", 값)` | Object |
| session에서 꺼내기 | `session.getAttribute("이름")` | Object (형변환 필요) |

- **Parameter**: 사용자가 form에 입력해서 **들어온** 값 (String, 읽기만 가능)
- **Attribute**: 서버(내 코드)가 **직접 저장하고 꺼내는** 값 (Object, 아무거나)

### 4-5. request 전달: forward와 함께

```jsp
<%-- a.jsp --%>
<% request.setAttribute("msg", "안녕"); %>
<jsp:forward page="b.jsp" />

<%-- b.jsp --%>
<% String msg = (String) request.getAttribute("msg"); %>
<p><%= msg %></p>
```

- forward로 이동하면 request가 같이 가서 값을 쓸 수 있어요.
- 하지만 `<a href="c.jsp">`로 **새로 요청**하면 request는 새것이라서 값이 없어요. → 그때 쓰는 게 **session**이에요. (필기의 `a.jsp → b.jsp(forward) / c.jsp(session)`)

### 4-6. 예제: 로그인 처리 (교수님이 강조)

**흐름**: `login.jsp`(입력) → `loginProc.jsp`(확인, 저장) → `main.jsp`(로그인 상태 표시) → 로그아웃

```jsp
<%-- loginProc.jsp : 로그인 확인하고 session에 저장 --%>
<%
  String id = request.getParameter("id");
  String pw = request.getParameter("pw");

  if (id.equals("admin") && pw.equals("1234")) {
      session.setAttribute("userId", id);     // 사물함에 저장
      response.sendRedirect("main.jsp");       // 메인으로 이동
  } else {
      response.sendRedirect("login.jsp");
  }
%>
```

```jsp
<%-- main.jsp : 로그인했는지 확인 --%>
<%
  String userId = (String) session.getAttribute("userId");
  if (userId == null) {
%>
    <p>로그인이 필요합니다.</p>
<% } else { %>
    <p><%= userId %> 님 환영합니다.</p>
<% } %>
```

```jsp
<%-- logout.jsp --%>
<% session.invalidate(); %>      <%-- 사물함 비우기 --%>
```

> 위 로그인 코드는 수업에서 한 예제의 구조를 바탕으로 정리한 거예요. 아이디, 비밀번호 값과 `sendRedirect` 사용 여부는 **수업 필기·예제 코드와 꼭 비교**해서 맞춰주세요.

### 외울 것

- 전달 객체 4개와 범위: page < request < session < application
- `getParameter`(String, 입력값) / `setAttribute`, `getAttribute`(Object)
- HTTP는 stateless → 로그인 같은 상태는 **session**에 저장
- `session.setAttribute("userId", id)` / `session.getAttribute("userId")` / `session.invalidate()`

### 자주 하는 실수

- `getAttribute`는 Object를 돌려줘서 `(String)`처럼 **형변환**해야 해요.
- `getParameter`와 `getAttribute`를 헷갈리는 것. **form 입력값은 Parameter**, **내가 저장한 건 Attribute**예요.
- 로그인 안 한 사람이 `main.jsp`를 열면 `getAttribute` 결과가 `null`이에요. `null` 체크를 먼저 해야 해요.

---

## 5장. 데이터베이스와 MySQL 기본

### 5-1. 왜 데이터베이스가 필요할까요?

**비유**: 파일 하나에 적어두는 건 **메모장**이고, 데이터베이스는 **정리가 잘된 큰 도서관**이에요. 빠르게 찾고, 고치고, 여러 사람이 같이 써도 안 꼬여요.

- **DB (Database)**: 데이터를 모아둔 곳
- **DBMS**: DB를 관리해주는 프로그램 (우리는 **MySQL**) ← System S/W

### 5-2. 구조: 큰 것에서 작은 것으로

```
MySQL Server (DBMS)
  └─ Database (= Schema)         ← 도서관
       └─ Table                  ← 서가(책장 한 칸)
            ├─ Column (열)       ← 항목 이름 (제목, 가격 ...)
            └─ Record / Row (행) ← 데이터 한 줄 (책 한 권)
```

필기의 표에서 **ID | name 이 열(Column)**, 가로로 한 줄이 **행(Row, Record)** 이에요. 이렇게 표(Table) 모양으로 데이터를 저장하는 DB를 **RDB(관계형 DB, Relational)** 라고 해요.

### 5-3. MySQL 구성품 (필기)

| 이름 | 하는 일 |
|---|---|
| MySQL Server | DB를 실제로 돌리는 **서버 프로그램** (DBMS) |
| MySQL Workbench | 마우스로 쓰는 **GUI 클라이언트** |
| MySQL Command Line (Shell) | 글자로 명령을 치는 **CLI 클라이언트** |
| MySQL Router | 접속을 중간에서 이어주는 도구 |
| MySQL Connector (JDBC) | **Java 프로그램이 MySQL과 연결**하게 해주는 부품 |

- 서버의 접속 번호(포트)는 **3306**이에요. 접속은 `root@localhost:3306` 형태로 써요.
- 클라이언트로 접속해서 쓰는 사람을 **DBA**(DB 관리자)라고 해요.

### 5-4. 테이블 만들 때 알아둘 것 (필기의 user 표)

| user_id | name | email | point |
|---|---|---|---|
| char(10) | varchar(20) | varchar(...) | integer(10) |

| 타입 | 뜻 |
|---|---|
| `char(10)` | **고정** 10글자 (짧아도 10칸 차지) |
| `varchar(20)` | **최대** 20글자 (글자 수만큼만 차지) |
| `int` | 정수 |
| `decimal(10,2)` | 전체 10자리, 소수 2자리까지의 실수 |
| `date` / `datetime` | 날짜 / 날짜+시간 |
| `bool` | 참/거짓 |

- **Primary Key (기본키)**: 행마다 겹치지 않는 **대표 번호**. (필기의 `bookid`, 학번처럼요)
- **Not Null (NN)**: 비워두면 안 되는 칸
- **Auto Increment (AI)**: 값을 안 줘도 **자동으로 1, 2, 3...** 올라가는 번호

### 5-5. SQL 명령어는 3종류로 나눠요

**SQL = Structured Query Language** (구조화된 질의 언어)

| 종류 | 이름 | 하는 일 | 명령어 |
|---|---|---|---|
| **DDL** | 정의 | 판(DB, 테이블) **만들고 지우기** | `create`, `drop`, `alter` |
| **DML** | 조작 | 안의 **데이터 다루기** (CRUD) | `insert`, `select`, `update`, `delete` |
| **DCL** | 제어 | **권한** 주고 뺏기 | `grant`, `revoke` |

**CRUD**: Create(만들기=insert), Read(읽기=select), Update(고치기=update), Delete(지우기=delete)

> 비유: DDL은 **책장을 만드는 것**, DML은 **책장 속 책을 넣고 빼는 것**, DCL은 **출입 허가증**이에요.

### 5-6. 확인 명령어

```sql
show databases;      -- 데이터베이스 목록
show tables;         -- 현재 DB의 테이블 목록
desc book;           -- book 테이블의 열 구성 보기
```

### 5-7. 데이터베이스는 이 순서로 만들어요 (필기 오른쪽)

1. **요구 분석** : 무슨 기능이 필요하고 어떤 데이터가 있나?
2. **DB 설계** : 개념 스키마(**E-R 다이어그램**) → 물리 스키마(테이블 구조)
3. **DB 생성** : DDL(`create`)로 실제로 만들기

**정규화**: 한 테이블에 다 몰아넣지 않고, **필요한 컬럼끼리 여러 테이블로 쪼개는** 설계 작업이에요. (예: 회원 테이블과 PT 일정 테이블을 따로)

### 외울 것

- DBMS = MySQL, Database ⊃ Table ⊃ Column/Record
- DDL / DML / DCL의 의미와 대표 명령어
- CRUD = insert, select, update, delete
- Primary Key, Not Null, Auto Increment 뜻

### 자주 하는 실수

- `char`와 `varchar`: 고정 길이와 가변 길이를 바꿔 설명하기.
- DDL(구조)과 DML(데이터)을 헷갈리기. `create table`은 **DDL**, `insert`는 **DML**이에요.

---

## 6장. SQL (insert, select, update, delete)

### 6-0. 먼저 테이블 하나 만들어요 (수업에서 쓴 book 테이블)

```sql
create table book (
    bookid  int          not null auto_increment,
    title   varchar(20)  not null,
    pubdate date         not null,
    price   int          not null,
    rating  decimal(2,1),
    primary key (bookid)
);
```

| bookid | title | pubdate | price | rating |
|---|---|---|---|---|
| 1 | Java | 2025-01-01 | 20000 | 4.5 |
| 2 | JSP | 2025-01-04 | 25000 | 4.0 |

- `decimal(2,1)` : 전체 2자리, 소수 1자리 → `4.5` 같은 평점
- `bookid`는 `auto_increment`라서 **insert할 때 안 써도** 자동으로 들어가요.

> 수업에서 Workbench로 `book2` 테이블을 만들 때: 컬럼 이름 입력 → 타입 선택 → **PK(기본키), NN(Not Null), AI(자동증가)** 칸 체크 → Apply 순서였어요.

### 6-1. insert (넣기)

**비유**: 표 맨 아래에 **새 줄을 하나 추가**해요.

```sql
insert into book (title, pubdate, price, rating)
values ('JSP', '2025-01-04', 25000, 4.0);
```

- `insert into 테이블 (열 이름들) values (값들)` : **열 순서와 값 순서가 같아야** 해요.
- 문자와 날짜는 작은따옴표 `' '`로 묶어요. 숫자는 그냥 써요.
- `bookid`는 자동이라서 열 목록에서 **뺐어요.**

### 6-2. select (찾기) = Selection + Projection

```sql
select * from book;                              -- 전부
select title, price from book;                   -- 원하는 열만
select * from book where price >= 20000;        -- 조건에 맞는 행만
select title from book where rating > 4 and price < 30000;
```

select의 두 가지 일 (시험에 나오기 좋은 개념)

| 이름 | 뜻 | 코드 |
|---|---|---|
| **Selection (선택)** | 조건에 맞는 **행(레코드)** 고르기 | `where ...` |
| **Projection (투영)** | 보고 싶은 **열(컬럼)** 고르기 | `select 열이름` |

**비유**: 학생 명단에서 "3학년만 뽑고(Selection), 이름과 학번 칸만 본다(Projection)".

- `*` 는 "모든 열"이에요.
- `where`의 조건: `=`, `>`, `<`, `>=`, `<=`, `and`, `or` 를 쓸 수 있어요.
- SQL에서 "같다"는 `=` **하나**예요. (Java처럼 `==` 아니에요)

### 6-3. update (고치기)

```sql
update book
set price = 20000, rating = 5
where pubdate <= '2025/01/04';
```

- `update 테이블 set 열 = 값, 열 = 값 where 조건;`
- `set`에서 여러 개 바꿀 땐 **쉼표(,)** 로 이어요. 대입하듯 `열 = 값`으로 써요.
- 먼저 `where`로 **대상(행)을 고르고**, 그 행들만 바뀌어요.
- **`where`를 빼면 모든 행이 바뀌어요!**

### 6-4. delete (지우기)

```sql
delete from book
where bookid = 3;
```

- `delete from 테이블 where 조건;` ← **`from`까지 외워요.** (update는 `from` 없어요)
- **`where`를 빼면 모든 행이 지워져요!** 테이블 자체가 아니라 안의 데이터가 다 지워지는 거예요.

### 6-5. 4개 한눈에 비교 (교수님이 "외워야 한다"고 강조)

| 기능 | 문법 뼈대 |
|---|---|
| insert | `insert into 테이블 (열들) values (값들);` |
| select | `select 열들 from 테이블 where 조건;` |
| update | `update 테이블 set 열=값, ... where 조건;` |
| delete | `delete from 테이블 where 조건;` |

- 세 개(select, update, delete)는 **`where` 조건 쓰는 법이 똑같아요.**

### 6-6. join (개념만)

**비유**: 회원 명단 표와 PT 예약 표가 따로 있어요. "A 회원이 이번 달에 어떤 PT를 예약했지?"를 알려면 **두 표를 이어서** 봐야 해요. 이게 join이에요.

- 한 테이블에 다 넣지 않고 여러 테이블로 나눴기 때문에 필요한 연산이에요.
- 여러 테이블에 걸쳐 Selection + Projection을 하는 select예요.
- 교수님이 "이건 뒤에 가서 다시 본다"고 하셨어요. 이번 시험에서는 **개념(왜 필요한지)** 정도만 알면 돼요.

### 외울 것

- 4개 문법 뼈대 (위 표를 **백지에 써보기**)
- Selection = 행 고르기(where), Projection = 열 고르기(select 열)
- `update ... set ... where`, `delete from ... where`
- where가 없으면 전체가 바뀌거나 지워진다

### 자주 하는 실수

- `delete book where ...` 처럼 `from`을 빼먹기.
- `update` 에서 `set` 사이를 `and`로 이어서 쓰기. **쉼표(,)** 예요.
- 값에 따옴표를 빠뜨리기. 문자와 날짜는 `' '`.
- SQL 문 끝의 세미콜론(`;`) 빼먹기 (Java 안의 문자열 SQL에서는 안 붙여요).

---

## 7장. DAO, DTO 만들기 (오늘 수업)

### 7-1. 왜 DAO와 DTO가 필요할까요?

지난 시간에는 JSP **한 파일 안에서** 다 했어요. (`dbcon.jsp`)

1. DB 연결 → 2. SQL 작성 → 3. SQL 실행 → 4. 결과 출력 → 5. 연결 해제

JSP 안에 이 모든 걸 넣으면 코드가 길고 HTML과 뒤섞여서 지저분해져요.
JSP의 원래 역할은 **"보여주기"** 예요. 그래서 일을 나눠요.

**비유**: 식당에서 **홀 직원(JSP) / 주방 보조(DAO) / 쟁반(DTO)** 이에요.

| 이름 | 풀네임 | 정체 | 하는 일 | 비유 |
|---|---|---|---|---|
| **JSP** | - | JSP 파일 | 요청 받고 결과를 **출력** (Presentation) | 홀 직원 |
| **DAO** | **D**ata **A**ccess **O**bject | **Java 클래스** | **DB 연결, SQL 실행**, 결과 받기 | 창고에서 물건을 꺼내오는 사람 |
| **DTO** | **D**ata **T**ransfer **O**bject | **Java 클래스** | 데이터를 **담아서 전달**하는 그릇 | 쟁반, 상자 |

### 7-2. 흐름

```
 사용자 ──요청──▶ JSP ──요청──▶ DAO ──SQL──▶ DB
                                  │             │
                                  │◀── 결과 ────┘
                                  ▼
                            DTO(Book 객체)에 담기
                                  │
 사용자 ◀──출력── JSP ◀───────────┘
```

1. 사용자가 JSP 화면에서 입력, 버튼 클릭
2. JSP는 DB 일을 **직접 안 하고 DAO에 요청만** 해요
3. DAO가 DB 연결 → SQL 만들기 → 실행 → 결과 받기
4. 결과를 그냥 값이 아니라 **DTO 객체**(예: Book)로 포장해서 JSP에 넘겨요
5. JSP는 받은 객체를 **출력**만 해요

> **핵심 한 줄**: JSP는 "요청, 결과 받기, 출력", DAO는 "DB 작업 전부", DTO는 "데이터를 담는 그릇".

### 7-3. 준비: 패키지와 클래스 (Eclipse)

1. `src/main/java` 에서 마우스 오른쪽 → New → Package : `com.bookshop`
2. 그 패키지에 클래스 두 개: **`BookDAO`**, **`BookDTO`**

### 7-4. BookDTO (데이터 그릇)

**일반 데이터 클래스랑 똑같이** 만들어요. 변수 4개 + 생성자 + getter/setter.

```java
package com.bookshop;

public class BookDTO {
    private String title;
    private String pubdate;
    private int price;
    private double rating;

    // 생성자 (Source → Generate Constructor using Fields : 4개 모두 체크)
    public BookDTO(String title, String pubdate, int price, double rating) {
        this.title = title;
        this.pubdate = pubdate;
        this.price = price;
        this.rating = rating;
    }

    // getter / setter (Source → Generate Getters and Setters)
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getPubdate() { return pubdate; }
    public void setPubdate(String pubdate) { this.pubdate = pubdate; }
    public int getPrice() { return price; }
    public void setPrice(int price) { this.price = price; }
    public double getRating() { return rating; }
    public void setRating(double rating) { this.rating = rating; }
}
```

- 변수는 모두 **private**, 읽고 쓰는 건 **getter/setter**로 해요.
- DB에서 찾은 책 한 권 = `BookDTO` 객체 하나예요.

### 7-4-1. 변수 이름 (수업 필기와 맞추세요)

수업에서는 `dbcon.jsp`에 있던 **연결 정보 문자열 4개**를 그대로 복사해서 DAO 맨 위에 `private`로 넣었어요. 아래 코드의 변수명(`jdbcDriver` 등)과 DB 이름(`DB이름`)은 **수업 코드에 있던 이름으로** 바꿔서 외우세요.

### 7-5. BookDAO (1) 연결 정보 + 연결 함수

```java
package com.bookshop;

import java.sql.*;          // Connection, PreparedStatement, ResultSet 모두 포함

public class BookDAO {

    // ① DB 연결 정보 4개 (이 클래스 안에서만 쓰니까 private)
    private String jdbcDriver = "com.mysql.cj.jdbc.Driver";
    private String jdbcUrl    = "jdbc:mysql://localhost:3306/DB이름";
    private String dbId       = "root";
    private String dbPw       = "비밀번호";

    // ② 연결 함수 (클래스 안에서만 쓰니까 private)
    private Connection getConnection() throws ClassNotFoundException, SQLException {
        Class.forName(jdbcDriver);                                   // 드라이버 로딩
        return DriverManager.getConnection(jdbcUrl, dbId, dbPw);     // 연결 만들어 돌려줌
    }
```

- `import java.sql.*;` : SQL 관련 클래스를 한 번에 가져와요. (`*`는 전부)
- `getConnection()`이 던지는 예외 2개: **ClassNotFoundException**(드라이버 못 찾음), **SQLException**(연결 실패)
- `throws`는 "예외를 내가 처리하지 않고, **나를 부른 쪽으로 넘길게**"라는 뜻이에요. (Eclipse의 *Add throws declaration*)

### 7-6. BookDAO (2) 책 추가: `addNewBook` (insert, **Create**)

```java
    // 외부(JSP)에서 호출해야 하니까 public
    public boolean addNewBook(String title, String pubdate, int price, double rating)
            throws SQLException {

        Connection conn = null;
        PreparedStatement stmt = null;
        int result = 0;                       // insert한 레코드 개수를 받을 변수

        try {
            conn = getConnection();                                     // ① DB 연결

            String sql = "insert into book (title, pubdate, price, rating) "
                       + "values (?, ?, ?, ?)";                         // ② SQL 작성
            stmt = conn.prepareStatement(sql);                          // SQL을 담을 그릇

            stmt.setString(1, title);                                   // 1번 ? 에 title
            stmt.setString(2, pubdate);                                 // 2번 ? 에 pubdate
            stmt.setInt(3, price);                                      // 3번 ? 에 price
            stmt.setDouble(4, rating);                                  // 4번 ? 에 rating

            result = stmt.executeUpdate();                              // ③ SQL 실행
        } catch (Exception e) {
            e.printStackTrace();
        } finally {                                                     // ⑤ 연결 해제
            if (stmt != null) stmt.close();
            if (conn != null) conn.close();
        }
        return result > 0;                                              // 1개 이상이면 true
    }
```

**한 줄씩 이해하기**

| 코드 | 뜻 |
|---|---|
| `PreparedStatement` | SQL을 **DB에 전달하는 매개체** (택배 상자) |
| `?` | 값이 들어갈 **빈칸**. 나중에 하나씩 채움 |
| `setString(1, ...)` | **1번째** `?` 에 문자열을 채움 (번호는 **1부터**) |
| `executeUpdate()` | insert, update, delete 실행 → **영향받은 행 개수(int)** 를 돌려줌 |
| `result > 0` | 1이면 true, 0이면 false (if를 쓸 필요 없이 한 줄로) |
| `finally` | 성공하든 실패하든 **무조건 실행** → 연결 닫기 |

- 타입에 맞는 set 메서드: 문자, 날짜는 `setString`, 정수는 `setInt`, 실수는 `setDouble`
- `catch`에서는 `e.printStackTrace()`로 오류를 찍어요.
- try 안에서 `return`하지 않고, **try 바깥에서 `return result > 0;`** 해요. (안 그러면 "return이 없다"는 빨간 줄이 떠요)

### 7-7. BookDAO (3) 제목으로 찾기: `findBookByTitle` (select, **Read**)

```java
    public BookDTO findBookByTitle(String title) throws SQLException {

        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;                    // select 결과(레코드 집합)를 받을 변수
        BookDTO book = null;                    // 찾은 책 한 권을 담을 DTO

        try {
            conn = getConnection();

            String sql = "select * from book where title = ?";
            stmt = conn.prepareStatement(sql);
            stmt.setString(1, title);

            rs = stmt.executeQuery();           // select 실행 → 레코드 집합

            while (rs.next()) {                 // 다음 레코드로 이동, 있으면 true
                book = new BookDTO(
                    rs.getString("title"),
                    rs.getString("pubdate"),
                    rs.getInt("price"),
                    rs.getDouble("rating")
                );
                break;                          // 같은 제목이 여러 개여도 첫 번째만
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (rs != null) rs.close();
            if (stmt != null) stmt.close();
            if (conn != null) conn.close();
        }
        return book;                            // 못 찾으면 null
    }
}
```

**핵심 포인트**

- select는 `executeUpdate()`가 아니라 **`executeQuery()`** 를 써요. 결과는 숫자가 아니라 **`ResultSet`(레코드 집합)** 이에요.
- **`rs.next()`**: 레코드 집합 안에는 **포인터**가 있어서, `next()`를 부를 때마다 다음 한 줄로 이동해요. 있으면 `true`, 끝이면 `false` → `while (rs.next())`로 한 줄씩 꺼내요.
- 꺼낼 때는 열 타입에 맞게 `rs.getString("열이름")`, `rs.getInt(...)`, `rs.getDouble(...)`.
- 꺼낸 값으로 **`new BookDTO(...)`** 를 만들어 책 한 권을 담고 돌려줘요. 이게 DTO의 역할이에요.
- 못 찾으면 `book`은 처음 값 그대로 **`null`** 이에요. 그래서 JSP에서 `null` 검사를 해요.

**executeUpdate와 executeQuery 비교**

| | executeUpdate() | executeQuery() |
|---|---|---|
| 용도 | insert, update, delete | select |
| 돌려주는 값 | **int** (영향받은 행 개수) | **ResultSet** (레코드 집합) |

### 7-8. JSP 쪽 ① 입력 화면 (add2.jsp)

form으로 입력값을 받고, `action`으로 처리 JSP에 보내요. (HTML 문법은 시험 범위 밖이니 흐름만)

```jsp
<h1>신규 도서 등록</h1>
<form action="addBookProc.jsp" method="post">
    제목 : <input type="text" name="title"><br>
    출간일 : <input type="text" name="pubdate"><br>
    가격 : <input type="text" name="price"><br>
    평점 : <input type="text" name="rating"><br>
    <input type="submit" value="도서 등록">
</form>
```

- 입력칸의 **`name`** 이 `getParameter("...")`에서 쓰는 이름이에요.

### 7-9. JSP 쪽 ② 처리 (addBookProc.jsp)

```jsp
<%@ page import="com.bookshop.BookDAO" %>

<%
  // 1. 입력값 읽기 (전부 String으로 옴)
  String title   = request.getParameter("title");
  String pubdate = request.getParameter("pubdate");
  int    price   = Integer.parseInt(request.getParameter("price"));      // String → int
  double rating  = Double.parseDouble(request.getParameter("rating"));   // String → double

  // 2. DAO 객체 만들어서 일 시키기
  BookDAO dao = new BookDAO();
  boolean ok = dao.addNewBook(title, pubdate, price, rating);

  // 3. 결과에 따라 출력만
  if (ok) {
%>
    <h1>신규 도서 등록 완료</h1>
<% } else { %>
    <h1>도서 등록 실패</h1>
<% } %>
```

- `<%@ page import="..." %>` : 다른 패키지의 클래스를 쓰려고 **import**해요.
- **JSP는 DB 일을 안 해요.** DAO를 만들어서(`new BookDAO()`) 부탁만 하고, 결과를 출력하는 일만 해요.
- 같은 이름의 책을 또 등록해도 **들어가요.** `bookid`가 자동 번호라서 제목이 같아도 겹치지 않기 때문이에요.
- 등록 직후 **새로고침**하면 같은 요청이 한 번 더 가서 **똑같은 책이 두 번 등록돼요.** (수업에서 직접 확인함)

### 7-10. JSP 쪽 ③ 검색 (findBook.jsp)

```jsp
<%@ page import="com.bookshop.BookDAO, com.bookshop.BookDTO" %>

<%
  String title = request.getParameter("title");

  BookDAO dao = new BookDAO();
  BookDTO book = dao.findBookByTitle(title);     // 결과를 DTO로 받음

  if (book != null) {                            // null이 아니면 찾은 것
%>
    <h1>도서 검색 완료</h1>
    <p>제목 : <%= book.getTitle() %></p>
    <p>가격 : <%= book.getPrice() %></p>
<% } else { %>
    <h1>도서 검색 오류</h1>
<% } %>
```

- `BookDAO`와 `BookDTO` **두 클래스를 모두 import**해야 해요.
- 결과가 `null`인지 확인해서 **찾음/못 찾음**을 나눠 출력해요.
- 출력은 DTO의 **getter**(`book.getTitle()`)로 해요.

### 7-11. 전체 그림 정리 (이 한 장을 백지에 그려보기)

| 단계 | 누가 | 무엇을 |
|---|---|---|
| ① 입력 | add2.jsp / 검색 입력 | 사용자가 값 입력 |
| ② 받기 | addBookProc.jsp / findBook.jsp | `request.getParameter()`로 읽고 형변환 |
| ③ 요청 | JSP → **DAO** | `dao.addNewBook(...)`, `dao.findBookByTitle(...)` |
| ④ DB 일 | **DAO** | 연결 → SQL → 실행 → 결과 → 해제 |
| ⑤ 포장 | DAO → **DTO** | 찾은 데이터를 `BookDTO`에 담기 |
| ⑥ 출력 | JSP | 결과 받아 화면에 출력 |

### 외울 것

- DAO = Data Access Object (DB 연결, SQL 실행), DTO = Data Transfer Object (데이터 담는 그릇), JSP = 출력
- JDBC 5단계: **연결 → SQL 작성 → 실행 → 결과 처리 → 해제**
- insert/update/delete = `executeUpdate()` (int) / select = `executeQuery()` (ResultSet)
- `setString(번호, 값)` 번호는 **1부터**, `rs.next()`로 한 줄씩
- `finally`에서 `close()`

### 자주 하는 실수

- `?`의 개수와 `setXxx`의 개수·번호가 안 맞음. 4개면 1, 2, 3, 4번.
- 타입 안 맞춤: 가격(int)에 `setString` 쓰기, 또는 `getParameter` 결과를 형변환 없이 쓰기.
- select에 `executeUpdate()`를 쓰기. select는 **`executeQuery()`** 예요.
- `finally`에서 close를 빼먹으면 연결이 계속 남아요.
- 못 찾았을 때 `null`인 것을 검사하지 않고 `book.getTitle()`을 부르면 **NullPointerException**이 나요.

---

## 8장. 백지 연습문제

**방법**: 정답 페이지를 가리고, 빈 종이(굿노트)에 쓰고 비교하세요. 틀린 문제만 다시 풀어요.

1. 브라우저에서 `test.jsp`를 요청했을 때 서버에서 일어나는 일을 순서대로 쓰세요.
2. `<%! %>`, `<% %>`, `<%= %>` 각각의 역할을 한 줄씩 쓰세요.
3. `calc.jsp`: 입력받은 `a`, `b`(정수)를 더해서 화면에 출력하는 코드를 쓰세요.
4. `<jsp:include>`와 `<jsp:forward>`의 차이를 설명하세요.
5. 전달 객체 4개를 범위가 좁은 것부터 쓰세요.
6. `request.getParameter()`와 `request.getAttribute()`의 차이를 쓰세요.
7. HTTP가 stateless인데 로그인 상태를 어떻게 유지하나요? 코드로 `userId`를 저장하고 꺼내는 방법을 쓰세요.
8. DDL / DML / DCL 의 뜻과 각각 대표 명령어를 쓰세요.
9. `book` 테이블(title, pubdate, price, rating)에 책 한 권을 넣는 SQL을 쓰세요.
10. `book`에서 가격이 20000 이상인 책의 제목만 찾는 SQL을 쓰세요. (Selection, Projection 표시)
11. `rating`을 5로 바꾸되 `bookid`가 3인 책만 바꾸는 SQL과, 그 책을 지우는 SQL을 쓰세요.
12. DAO와 DTO가 무엇이고, JSP에 모든 걸 넣지 않고 나누는 이유를 설명하세요.
13. `BookDAO`의 `getConnection()` 함수를 쓰세요. (private, 예외 처리 포함)
14. `findBookByTitle(String title)`에서 `select` 실행 후 `ResultSet`에서 책 하나를 꺼내 `BookDTO`로 만드는 부분을 쓰세요.

---

<h2>정답</h2>

1. 요청 → Tomcat이 `test.jsp`를 **서블릿(`test_jsp.java`)으로 변환** → **컴파일**(`.class`) → **JVM이 실행** → 결과 **HTML을 응답**으로 전송.
2. `<%! %>` 선언: 변수, 함수 만들기(클래스 멤버) / `<% %>` 스크립틀릿: 연산, if, for 등 Java 코드 실행 / `<%= %>` 표현식: 값을 화면에 출력.
3. 코드:
   ```jsp
   <%
     int a = Integer.parseInt(request.getParameter("a"));
     int b = Integer.parseInt(request.getParameter("b"));
   %>
   a + b = <%= a + b %>
   ```
4. include는 다른 페이지를 **포함**하고 실행 후 **원래 페이지로 돌아옴**(결과가 합쳐짐, 머리·메뉴·푸터 재사용). forward는 처리를 **다른 페이지로 넘기고 돌아오지 않음**(request도 함께 전달, 주소창은 그대로).
5. `page` → `request` → `session` → `application`
6. `getParameter`: form으로 **들어온 입력값**을 읽음(**String**). `getAttribute`: 서버 코드가 `setAttribute`로 **저장한 객체**를 꺼냄(**Object**, 형변환 필요).
7. **session**에 저장한다.
   ```jsp
   session.setAttribute("userId", id);                      // 저장
   String userId = (String) session.getAttribute("userId"); // 꺼내기
   session.invalidate();                                    // 로그아웃
   ```
8. DDL = 데이터 정의(`create`, `drop`, `alter`) / DML = 데이터 조작(`insert`, `select`, `update`, `delete`) / DCL = 권한 제어(`grant`, `revoke`).
9. `insert into book (title, pubdate, price, rating) values ('JSP', '2025-01-04', 25000, 4.0);`
10. `select title from book where price >= 20000;` → `where price >= 20000` 이 **Selection**, `select title` 이 **Projection**.
11. `update book set rating = 5 where bookid = 3;` / `delete from book where bookid = 3;`
12. **DAO**: DB 연결, SQL 실행, 결과 받기를 맡는 Java 클래스. **DTO**: DB에서 찾은 데이터를 담아 JSP로 전달하는 데이터 클래스(객체). 나누는 이유: JSP는 **화면 출력**만 하게 하고, DB 작업을 분리해야 코드가 단순하고 관리하기 쉽다. (JSP에 다 넣으면 Java와 HTML이 뒤섞여 복잡)
13. 코드:
    ```java
    private Connection getConnection() throws ClassNotFoundException, SQLException {
        Class.forName(jdbcDriver);
        return DriverManager.getConnection(jdbcUrl, dbId, dbPw);
    }
    ```
14. 코드:
    ```java
    rs = stmt.executeQuery();
    while (rs.next()) {
        book = new BookDTO(
            rs.getString("title"),
            rs.getString("pubdate"),
            rs.getInt("price"),
            rs.getDouble("rating"));
        break;
    }
    ```

---

## 최종 체크리스트

- [ ] JSP 실행 과정(변환 → 컴파일 → 실행 → HTML)을 설명할 수 있다
- [ ] 스크립트 태그 3종 + 지시자의 쓰임을 구분한다
- [ ] `getParameter` 결과가 String이라 형변환이 필요한 걸 안다
- [ ] include와 forward의 차이를 말할 수 있다
- [ ] 전달 객체 4개와 session으로 로그인 상태를 유지하는 방법을 쓸 수 있다
- [ ] DDL/DML/DCL, CRUD를 구분한다
- [ ] insert, select, update, delete 문법 뼈대를 **외워서** 쓸 수 있다
- [ ] Selection과 Projection을 설명할 수 있다
- [ ] DAO, DTO, JSP의 역할을 설명하고 그림으로 그릴 수 있다
- [ ] `addNewBook`, `findBookByTitle`, `BookDTO`를 백지에 쓸 수 있다
- [ ] 시험: **10/20(화) 15:30**, 수업하던 강의실. 신분증, 필기구 챙기기

---

## 필기와 대조할 부분 (확인 부탁)

- 4장 표의 `getParameter` / `setAttribute` 구분: 필기 오른쪽 위에 `set/get Parameter (String)` 이라고 적혀 있는데, 실제로 **`setParameter`라는 메서드는 없어요.** Parameter는 읽기(`get`)만, 저장·꺼내기는 **Attribute**예요.
- 필기에서 `MongoDB, postgre → NoSQL`로 묶인 부분: **PostgreSQL은 NoSQL이 아니라 관계형(RDB)** 이에요. 시험 전에 필기를 고쳐두세요.
- 7장 DAO 변수명, DB 이름, 비밀번호는 수업 코드에서 쓴 것으로 맞춰서 외우세요.
- 로그인 예제(4장)는 수업 흐름을 바탕으로 정리한 코드라서, 수업 때 만든 파일명과 다를 수 있어요.
