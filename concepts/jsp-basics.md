## 큰 그림 (계층 구조)
Java     → JSP의 기반 언어 (JavaScript와는 완전히 별개)
Tomcat   → JSP 코드를 실행하고 결과를 HTML로 만들어 보내는 웹 서버
Eclipse  → JSP 프로젝트를 만들고 편집하는 개발 도구(IDE)
JSP      → HTML 안에 Java 코드를 끼워 넣어, 서버에서 동적으로 페이지를 만드는 기술

## JSP와 JavaScript는 다른가
완전히 다름. JSP는 Java 기반 서버 기술, JavaScript는 원래 브라우저 화면 담당 언어.
이름이 비슷할 뿐 문법도, 실행 위치도, 목적도 다름.

## 정적 페이지 vs 동적 페이지
- 정적(순수 HTML): 누가 봐도 항상 같은 내용
- 동적(JSP): 상황에 따라 내용이 달라짐 (로그인 정보, DB 조회 결과 등)

## JSP 문법 3종류 (Index.jsp 예제 기준)
- `<%@ ... %>` (디렉티브): 페이지 설정 선언. 예: 언어, 인코딩
- `<% ... %>` (스크립틀릿): 순수 Java 코드 실행 구간. 변수 선언, 로직 처리
- `<%= ... %>` (표현식): Java 값을 HTML 화면에 그대로 출력

## 요청-응답 흐름
1. 브라우저가 .jsp 파일 요청
2. Tomcat이 파일을 찾아 실행
3. <% %> 안의 Java 코드 실행 (변수 계산 등)
4. <%= %> 자리에 결과값을 끼워 넣어 완성된 HTML 생성
5. 완성된 순수 HTML(Java 코드는 이미 사라진 상태)을 브라우저로 전송
6. 브라우저는 HTML만 받아서 화면에 표시 (Java를 몰라도 됨)

## Java 클래스 구조 (Menu, OrderItem 예제 기준)
- **필드(field)**: 클래스가 담는 데이터. 보통 `private`로 선언해 외부에서 직접 접근 못 하게 함
- **생성자(constructor)**: `new 클래스명(값...)` 호출 시 자동 실행되어 필드를 초기화. `this.필드 = 매개변수`로 구분
- **getter/setter**: `private` 필드에 접근하는 유일한 공개 통로. `getX()`로 값을 꺼내고 `setX(값)`으로 값을 바꿈

## 클래스를 역할별로 분리하기
- Menu(메뉴판 항목: 이름, 단가)와 OrderItem(주문 내역: 이름, 수량, 총액)처럼, 목적이 다르면 별도 클래스로 설계

## JSP 액션 태그
- `<jsp:include page="파일.jsp" />`: 다른 페이지를 현재 위치에 끼워 넣음 (헤더/푸터처럼 반복되는 부분을 재사용할 때 유용, React의 공용 컴포넌트와 비슷한 개념)
- `<jsp:forward page="파일.jsp" />`: 현재 페이지 처리를 멈추고 다른 페이지로 완전히 넘김 (예: 데이터를 못 찾았을 때 에러 페이지로 이동)
- `<jsp:useBean id="이름" class="클래스경로" scope="범위" />`: 지정한 클래스의 객체를 생성
- `<jsp:setProperty property="*" name="이름" />`: 폼에서 넘어온 파라미터들을 useBean으로 만든 객체의 필드에 자동으로 채워넣음 (필드명과 input name이 일치해야 함)

## request 객체로 폼 데이터 받기
- `getParameter("이름")`: 값 1개를 String으로
- `getParameterValues("이름")`: 같은 이름의 값 여러 개를 String[]으로 (체크박스)
- `getParameterNames()`: 모든 파라미터 이름 (Enumeration, `while (hasMoreElements())`로 순회)
- `getParameterMap()`: 전체를 Map<String, String[]>으로 (`keySet()`으로 순회)
- `request.setCharacterEncoding("utf-8")`: 한글 입력값이 깨지지 않게 파라미터를 읽기 전에 호출
- 클라이언트 정보: `getRemoteAddr()`(IP), `getRemotePort()`, `getRequestURL()`, `getMethod()`

## 세션으로 로그인/로그아웃 처리
- 로그인: `session.setAttribute("userId", uid)`로 로그인 정보를 세션에 기록
- `session.getId()`: 세션 ID, `session.getMaxInactiveInterval()`: 타임아웃(초)
- 로그아웃: `session.invalidate()`로 세션 객체 자체를 소멸
- `getAttribute()`는 Object를 반환하므로 `(String)` 등으로 형변환 필요

## 내장객체의 유효 범위 (page / request / session / application)
- 네 객체 모두 `setAttribute("이름", 값)` / `getAttribute("이름")`으로 데이터를 저장하고 꺼냄 (getAttribute는 Object 반환 → 형변환 필요)
- **page** (`pageContext`): 현재 JSP 페이지 안에서만 유효, 페이지 처리가 끝나면 소멸 (`useBean`의 기본 scope)
- **request**: 한 번의 요청 동안 유효, forward/include된 페이지까지 공유, 응답이 끝나면 소멸 → 폼 파라미터 읽기, forward로 데이터 전달
- **session**: 같은 사용자(브라우저) 단위로 여러 요청에 걸쳐 유지, 타임아웃 또는 `invalidate()`로 소멸 → 로그인 정보, 장바구니, 상품 목록
- **application**: 웹 애플리케이션 전체에서 모든 사용자가 공유, 서버(앱) 종료 시 소멸 → 방문자 수, 공통 설정값
- 범위 선택 기준: 필요한 만큼 가장 짧은 범위를 사용 (넓을수록 메모리를 오래 차지하고, application은 동시 수정 문제 가능)

## 헷갈렸던 점
- JSP와 JavaScript는 이름만 비슷, 완전 별개 (Java 계열 vs JavaScript 계열)
- 브라우저에 도착하는 건 이미 Java가 실행되고 사라진 순수 HTML뿐
- 자기 스스로 닫는 태그(`<jsp:forward .../>`)와 여는/닫는 태그 쌍(`<h4>...</h4>`)을 혼동하지 않기
- HTML 태그는 여닫는 이름이 달라도 브라우저가 어느 정도 봐주지만, 정확한 문법(`<h4>...</h4>`)을 지키는 습관이 필요
- 체크박스를 하나도 선택하지 않으면 `getParameterValues()`는 빈 배열이 아니라 null을 반환 → 반복문 전에 null 체크 필요
- 오타를 고치다가 새 오타를 만들 수 있으니 수정 후 다시 확인하기 (`</h5>` → `</4>`, 정답은 `</h4>`)
- `useBean`의 기본 scope는 page라서, forward된 다른 페이지에서는 그 객체가 보이지 않음 (다른 페이지에서 쓰려면 request 이상의 범위 필요)