# 스크립트프로그래밍 중간고사 쉬운 정리

> **시험** 10/22(목) 15:30 (교수님 출석 처리 후 **15:40쯤 시작** 예상) · 장소 **412호** (10/15 수업 안내, 공지로 재확인) · 범위는 **10/19(월) 수업(reducer)까지**
> **형태** 수업 예제 중심. 문법을 **외워서 직접 쓰는** 문제 (예: "map으로 배열을 바꾸는 코드를 쓰시오")

**이 문서 읽는 법**
각 장은 이 순서예요: 비유(쉬운 그림) → 개념 → 코드 → 외울 것 → 자주 하는 실수 → **시험 답안용 서술**.
**비유는 이해용**이고, 시험 답안에는 각 장 끝의 **「시험 답안용 서술」** 의 정식 용어와 문장을 쓰세요.
코드는 눈으로만 보지 말고, 장마다 **백지에 직접 써보세요.** 시험이 "쓰는 문제"라서요.

**교수님이 말한 시험 형태 (10/15, 10/19 수업)**
- 예제처럼 **빈칸 코드를 손으로 쓰는 문제**: 예) "버튼 클릭 때마다 count를 1 감소시키는 구문", "dispatch하는 구문", "onChange 안에 들어갈 구문"
- **개념 설명 문제**: 예) "상태변수가 immutable하다는 의미를 설명하시오"
- 어렵게 내지 않고 **기본 사항**을 묻는다고 했어요. **문장 하나하나의 의미**를 알고 있으면 조금 바뀌어도 쓸 수 있어요.

**교수님이 짚은 순서 = 이 문서의 순서**

| 장 | 내용 | 시험에서 |
|---|---|---|
| 1 | JavaScript 문법 | 코드를 쓰는 문제 |
| 2 | 웹의 동작 과정 | 설명하는 문제 |
| 3 | JSX와 컴포넌트 | 코드, 설명 |
| 4 | 렌더링(화면 그려지는) 과정 | 설명하는 문제 |
| 5 | useState (상태, prev, 버튼) | 코드를 쓰는 문제 |
| 6 | useEffect | 코드, 설명 |
| 7 | 메모이제이션 | 설명, 코드 |
| 8 | Context | 설명, 코드 |
| 9 | useRef | 코드, 설명 |
| 10 | useReducer | 코드, 설명 |
| 11 | 백지 연습문제 + 정답 | 최종 점검 |

---

## 1장. JavaScript 문법

### 1-1. 함수와 화살표 함수

**비유**: 함수는 **자판기**예요. 돈과 버튼(입력)을 넣으면 음료(출력)가 나와요.

```js
function add(a, b) {
  return a + b;
}

const add = (a, b) => {
  return a + b;
};

const add = (a, b) => a + b;
```

- 위 세 개는 모두 같은 함수예요.
- 세 번째처럼 `{ }`를 없애고 한 줄로 쓰면 `return`이 자동으로 들어가요.
- 리액트에서는 `=>` (화살표 함수)를 거의 항상 써요.

### 1-2. 조건문

```js
if (age > 19) {
  console.log('성인');
} else if (age > 13) {
  console.log('청소년');
} else {
  console.log('어린이');
}

const msg = age > 19 ? '성인' : '미성년';

isLogin && console.log('로그인 상태');
```

- **삼항 연산자** `조건 ? 참일 때 : 거짓일 때` → if를 한 줄로 쓴 거예요.
- **`&&`**: 앞이 참일 때만 뒤를 실행해요. 리액트 화면에서 "조건이 참일 때만 보여줘"에 많이 써요.

### 1-3. 반복문

```js
for (let i = 0; i < 5; i++) {
  console.log(i);          // 0 1 2 3 4
}

for (const x of arr) {
  console.log(x);          // 배열 요소를 하나씩
}
```

- `i++`는 i를 1씩 올린다는 뜻이에요.

### 1-4. 배열 메서드 4총사 (시험 핵심)

먼저 **고차 함수**라는 말을 알아야 해요. "함수를 재료로 받는 함수"라는 뜻이에요.
`a.map(...)`의 괄호 안에 넣는 함수를 **콜백 함수(람다)**라고 불러요.

**비유로 먼저 이해해요**

- **map = 붕어빵 틀**: 반죽(원본)을 하나씩 넣으면, 같은 개수의 붕어빵(결과)이 나와요.
- **filter = 체**: 조건을 통과한 것만 남기고 나머지는 걸러요.
- **forEach = 출석 부르기**: 이름을 하나씩 부르기만 해요. 결과물은 없어요.
- **reduce = 계산기 누적**: 하나씩 더해서 값 하나로 만들어요.

```js
const a = [1, 2, 3, 4, 5];

const b = a.map((value, idx) => {
  return value + 1;
});
// b = [2, 3, 4, 5, 6]   (a는 그대로)

const c = a.filter(v => v % 2 === 0);
// c = [2, 4]

a.forEach(v => console.log(v));
// 1 2 3 4 5 를 출력만 함 (결과 없음)

const sum = a.reduce((acc, v) => acc + v, 0);
// sum = 15
```

| 메서드 | 결과 | 한 줄 요약 |
|---|---|---|
| `map` | 같은 길이의 **새 배열** | 모든 요소를 변환 |
| `filter` | 조건 통과한 **새 배열** | 걸러내기 |
| `forEach` | **없음** (undefined) | 하나씩 실행만 |
| `reduce` | **값 하나** | 누적 계산 |

> **외울 것: map 기본 틀**
> `배열.map((값, 인덱스) => { return 변환한 값; })`
> 인덱스를 안 쓰면 생략: `배열.map(v => v * 2)`

> **자주 하는 실수**: `forEach`는 결과가 없어서 `const r = a.forEach(...)`로 받아봤자 `undefined`예요.
> 값을 만들어야 하면 `map`을 쓰세요. (JSX에서 화면에 목록을 그릴 때도 `map`)

### 1-5. 객체(object)

**비유**: 객체는 **학생증**이에요. 이름, 학번처럼 "이름표 + 값"이 짝으로 들어 있어요.

```js
const user = { name: 'Lee', age: 20 };

user.name          // 'Lee'
user.age = 21;     // 값 바꾸기
```

### 1-6. 구조분해 (꺼내서 변수로 만들기)

**비유**: 택배 상자를 뜯어서 물건을 바로바로 꺼내 쓰는 거예요.

```js
const [x, y] = [10, 20];       // 배열: 순서대로
// x = 10, y = 20

const { name, age } = user;    // 객체: 이름표로
// name = 'Lee', age = 20

const { name, ...info } = user;
// info = { age: 20 }  (나머지는 info에)
```

- 리액트에서 `const [count, setCount] = useState(0)`가 바로 **배열 구조분해**예요.
- 컴포넌트에서 `({ width, height })`로 props를 받는 것이 **객체 구조분해**예요.

### 1-7. 스프레드 연산자 `...` (복사기)

**비유**: 상자 안의 물건을 전부 꺼내서 **새 상자**에 옮겨 담는 거예요.

```js
const a = [1, 2, 3];
const b = [...a, 4];        // [1, 2, 3, 4]

const user = { name: 'Lee', age: 20 };
const u2 = { ...user, age: 21 };
// { name: 'Lee', age: 21 }  (age만 덮어씀)

const key = 'email';
const u3 = { ...user, [key]: 'a@b.c' };
// [key]: 변수의 값이 키 이름이 됨
```

### 1-8. 왜 "원본을 고치지 말고 새로 만들까?" (불변성)

이게 리액트 전체를 이해하는 열쇠예요.

**비유**: 배열이나 객체 변수는 **집 주소가 적힌 쪽지**예요. 집(데이터)은 따로 있고, 변수는 주소만 들고 있어요.

- `a.push(4)`: 집 안의 가구만 바꿔요. 쪽지(주소)는 **그대로**예요.
- `a = [...a, 4]`: **새 집**을 지어서 쪽지의 주소를 새 집으로 바꿔요.

리액트는 "쪽지가 바뀌었나?"만 확인해요. 가구만 바꾸면 "쪽지 그대로네? 안 바뀌었네" 하고 **화면을 안 그려요.**
그래서 상태(state)는 항상 `...`로 **새 배열, 새 객체**를 만들어서 바꿔요.

```js
a.push(4);          // 원본 변경 (state에는 금지)
a.y = 3;            // 안쪽 값만 변경 (금지)
a = [...a, 4];      // 새로 만들어 교체 (정답)
```

### 시험 답안용 서술 (그대로 써도 되는 문장)

**함수와 화살표 함수**
- **화살표 함수(Arrow Function)**: `(매개변수) => 반환값` 형태로 함수를 **간결하게 작성**하는 문법이다. 중괄호 `{ }`와 `return`을 생략하면 식의 결과가 **자동으로 반환**된다.

**조건 표현**
- **삼항 연산자**: `조건 ? 참일 때 값 : 거짓일 때 값`. if-else를 **한 줄로 표현**하며 값을 반환한다.
- **논리 AND(`&&`) 단축 평가**: 앞의 식이 **참일 때만** 뒤의 식을 실행(평가)한다. 리액트에서 **조건부 렌더링**에 쓴다.

**고차 함수와 콜백 함수**
- **고차 함수(Higher-order function)**: 함수를 **인자로 받거나 함수를 반환**하는 함수이다. (`map`, `filter`, `forEach`, `reduce`)
- **콜백 함수(Callback function)**: 다른 함수의 **인자로 전달**되어 그 함수 안에서 호출되는 함수이다.

**배열 메서드**

| 메서드 | 설명 (답안용) | 반환값 |
|---|---|---|
| `map` | 배열의 **모든 요소에 콜백 함수를 적용**하여 **새로운 배열**을 만든다. 원본은 변하지 않고 길이는 같다. | 새 배열 |
| `filter` | 콜백 함수의 결과가 **true인 요소만** 모아 **새로운 배열**을 만든다. | 새 배열 |
| `forEach` | 배열의 각 요소에 대해 콜백 함수를 **한 번씩 실행**한다. | 없음 (`undefined`) |
| `reduce` | 배열의 요소를 **누적**하여 **하나의 값**으로 만든다. | 하나의 값 |

**구조 분해 할당과 스프레드 연산자**
- **구조 분해 할당(Destructuring)**: 배열이나 객체의 값을 **꺼내서 변수에 한 번에 할당**하는 문법이다. 배열은 **순서**로, 객체는 **키 이름**으로 꺼낸다.
- **스프레드 연산자(`...`)**: 배열이나 객체의 요소를 **펼쳐서** 새로운 배열, 객체로 **복사·합치기**할 때 쓴다. (얕은 복사)

**불변성(Immutability)**
- 배열과 객체는 **참조형**이라 변수에는 **메모리 주소**가 저장된다. 리액트는 상태의 **주소(참조)가 바뀌었는지 비교**하여 변경을 감지하므로, 상태를 **직접 수정하지 않고 새로운 배열·객체를 만들어 교체**해야 한다.

---

## 2장. 웹의 동작 과정

### 2-1. 브라우저가 화면을 만드는 과정

**비유**: 식당이에요. 손님(클라이언트, 브라우저)이 주문하고, 주방(서버)이 음식을 내줘요.

1. 브라우저가 `hello.com/hello.html`을 서버에 **요청**해요.
2. 서버가 `hello.html`, `hello.css`, `hello.js` 파일을 **보내줘요.**
3. 브라우저가 받은 파일로 화면을 만들어요.

브라우저가 화면을 만드는 순서:
1. **파싱(passing)**: HTML 글자를 읽어요.
2. **DOM Tree**: HTML 구조를 **나무(트리) 모양**으로 정리해요.
3. **CSS Tree**: 스타일 규칙도 나무로 정리해요.
4. 둘을 합쳐서 **Render Tree**를 만들고 화면에 **그려요.**

> **DOM이란?** 브라우저가 HTML을 JS로 다룰 수 있게 만든 **객체 나무**예요.
> `document.getElementById("photo")`처럼 JS로 직접 만지는 것을 **DOM 직접 조작**이라고 해요.

### 2-2. MPA vs SPA (그리고 SSR vs CSR)

**비유**: **책 vs 화이트보드**예요.

- **MPA (Multi Page)**: 책장을 넘길 때마다 서버에서 **새 페이지를 통째로** 받아와요.
  예: `test.jsp`를 실행해서 HTML을 만들어 보내줌. 서버가 HTML을 완성해서 주는 방식이라 **SSR**(서버 사이드 렌더링)이에요.
- **SPA (Single Page)**: 첫 `index.html` **하나만** 받고, 그 안에서 JS(리액트)가 필요한 부분만 지웠다 다시 써요.
  브라우저가 화면을 만들어서 **CSR**(클라이언트 사이드 렌더링)이에요.

| 구분 | MPA | SPA |
|---|---|---|
| 페이지 | 이동마다 새로 받음 | 하나만 받고 일부만 교체 |
| HTML을 만드는 곳 | 서버 (SSR) | 브라우저 (CSR) |
| 예 | JSP | React |

### 2-3. 개발 도구 역할

- **Node.js**: 브라우저 밖에서도 JS를 실행하게 해주는 프로그램이에요.
- **npm**: 필요한 프로그램(패키지)을 내려받아 관리해요. **앱스토어**라고 생각하세요.
- **Vite**: 프로젝트 **뼈대를 만들고**, 개발 서버를 돌리고, JSX를 브라우저가 읽는 JS로 **변환**해요. (Build Tool, Bundler)
- **React**: 화면(UI)을 부품으로 만드는 **라이브러리**예요.

```
npx create-vite@latest hello-app
cd hello-app
npm install
npm run dev        → localhost:5173
```

실행 흐름: `index.html`(안에 `<div id="root">`) → `main.jsx` → `App.jsx`

```jsx
// main.jsx
createRoot(document.getElementById('root'))
  .render(<App />);
```

### 시험 답안용 서술 (그대로 써도 되는 문장)

**웹의 동작과 브라우저 렌더링**
- 웹은 **클라이언트-서버 구조**로, 브라우저가 서버에 **요청**하면 서버가 HTML, CSS, JS 파일을 **응답**하고 브라우저가 이를 해석해 화면에 출력한다.
- **브라우저 렌더링 과정**: HTML을 **파싱**하여 **DOM Tree**를 만들고, CSS를 파싱하여 **CSS Tree**를 만든 뒤, 둘을 합쳐 **Render Tree**를 만들어 화면에 **그린다.**
- **DOM(Document Object Model)**: HTML 문서를 **객체의 트리 구조**로 표현하여 JavaScript로 접근·조작할 수 있게 한 인터페이스이다.

**MPA와 SPA / SSR과 CSR**
- **MPA(Multi Page Application)**: 페이지를 이동할 때마다 서버에서 **새 HTML 페이지 전체**를 받아온다. 서버가 HTML을 완성해서 보내는 **SSR(서버 사이드 렌더링)** 방식이다. (예: JSP)
- **SPA(Single Page Application)**: **하나의 HTML**만 받아오고, 이후 **JavaScript가 화면의 필요한 부분만 갱신**한다. 브라우저에서 화면을 만드는 **CSR(클라이언트 사이드 렌더링)** 방식이다. (예: React)

**개발 도구**
- **Node.js**: 브라우저 밖에서도 JavaScript를 실행할 수 있게 하는 **JavaScript 런타임 환경**이다.
- **npm(Node Package Manager)**: 필요한 **패키지(라이브러리)를 설치하고 관리**하는 도구이다.
- **Vite**: 프로젝트 **생성, 개발 서버 실행, 빌드(JSX 변환 및 번들링)** 를 해주는 **빌드 도구**이다.
- **React**: **컴포넌트 기반**으로 사용자 인터페이스(UI)를 만드는 **JavaScript 라이브러리**이다.

---

## 3장. JSX와 컴포넌트

### 3-1. JSX란?

**비유**: 레고 설명서예요. "HTML처럼 생긴 글"로 화면 모양을 적으면 리액트가 그대로 만들어요.

화면을 JS로만 만들면 이렇게 힘들어요.

```js
const e = document.createElement("h1");
const text = document.createTextNode("Hello");
e.appendChild(text);
```

JSX로는 한 줄이에요: `<h1>Hello</h1>`

- 브라우저는 JSX를 못 읽어요. **Vite가 JS로 바꿔줘요.**
- 변환 결과: `React.createElement("h1", { className: 'title' }, "React")`
- JSX = **HTML + JS**를 섞어 쓰는 문법이에요.

### 3-2. JSX 규칙 3가지 (외우기)

1. **하나로 감싸기**: 맨 바깥은 요소 하나여야 해요. 감쌀 게 없으면 빈 태그 `<> ... </>`를 써요.
2. **class → className**: `class`는 JS에서 이미 쓰는 단어라서 `className`으로 써요.
3. **JS 값은 `{ }` 안에**: 변수, 계산, 함수 호출은 중괄호 안에 넣어요. 태그는 반드시 닫아야 해요 (`<br />`, `<input />`).

```jsx
function Header() {
  const name = '민수';
  return (
    <>
      <h1 className="title">안녕 {name}</h1>
      <p>{1 + 2}</p>
      <p style={{ color: 'red', fontSize: 20 }}>
        스타일
      </p>
    </>
  );
}
```

- `style={{ ... }}`: 바깥 `{ }`는 "JS가 시작"이고, 안쪽 `{ }`는 **객체**예요. 속성 이름은 `fontSize`처럼 낙타표기를 써요.

### 3-3. 컴포넌트

**비유**: 컴포넌트는 **레고 블록**이에요. 작은 블록(Header, Menu)을 조립해서 큰 화면(App)을 만들어요.

- 컴포넌트 = **대문자로 시작하는 함수**, JSX를 `return`해요.
- 조립 구조 예: `main` 아래에 `Header`, `ToolBar`, `ToolList`... 이렇게 **계층(나무)**을 이뤄요.
- (클래스형 컴포넌트도 있지만, 지금은 **함수형**을 써요.)

### 3-4. props (부모가 자식에게 보내는 택배)

```jsx
function Box({ width, height }) {
  return <p>{width} x {height}</p>;
}

function App() {
  return <Box width={4} height={6} />;
}
```

- 부모가 `width={4}`처럼 값을 보내면, 자식은 `props.width`로 받아요.
- 위처럼 `({ width, height })`로 **구조분해**해서 받으면 편해요.
- props는 **읽기 전용**이에요. 자식이 마음대로 못 바꿔요.

### 3-5. 목록 그리기: map + key

```jsx
const cars = [
  { id: 1, name: '소나타' },
  { id: 2, name: '아반떼' },
];

return (
  <ul>
    {cars.map(car => (
      <li key={car.id}>{car.name}</li>
    ))}
  </ul>
);
```

- 배열을 `map`으로 `<li>` 배열로 바꿔요. (`forEach`는 결과가 없어서 JSX에서 못 써요.)
- **key**는 각 항목의 **번호표**예요. 리액트가 항목을 구별하려고 필요하고, 고유한 `id`를 넣어요.

### 3-6. 조건부 화면

```jsx
{loading && <p>불러오는 중...</p>}

{todos.length === 0
  ? <p>할 일이 없어요</p>
  : <p>할 일 {todos.length}개</p>}
```

### 3-7. 입력창과 버튼

```jsx
<input
  type="text"
  value={text}
  onChange={e => setText(e.target.value)}
/>
```

- `e.target.value`: 사용자가 입력한 글자예요.
- `value={text}` + `onChange`를 같이 써야 입력창이 state와 연결돼요.

### 시험 답안용 서술 (그대로 써도 되는 문장)

**JSX**
- **JSX(JavaScript XML)**: JavaScript 안에서 **HTML과 비슷한 문법으로 UI를 작성**할 수 있게 한 **확장 문법**이다. 빌드 과정에서 `React.createElement()` 호출로 **변환**된다.
- **JSX 작성 규칙**
    1. 반드시 **하나의 루트 요소**로 감싼다. (`<div>` 또는 빈 태그 `<> </>`)
    2. HTML의 `class` 대신 **`className`** 을 쓴다.
    3. JavaScript 식은 **중괄호 `{ }`** 안에 쓰고, 모든 태그는 **닫아야** 한다. (`<input />`)

**컴포넌트(Component)**
- UI를 **독립적이고 재사용 가능한 단위**로 나눈 것으로, **JSX를 반환하는 함수**이다. 이름은 **대문자로 시작**한다.

**props**
- 부모 컴포넌트가 자식 컴포넌트에 **데이터를 전달**하는 수단이다. 자식에서는 **읽기 전용(read-only)** 이며 **부모 → 자식 단방향**으로 전달된다. 객체 구조 분해로 `({ width, height })`처럼 받는다.

**리스트 렌더링과 key**
- 배열을 화면에 반복 출력할 때는 **`map()`** 을 사용한다. 각 요소에는 **고유한 `key`** 를 지정해야 하며, 리액트가 **어떤 항목이 추가·삭제·변경되었는지 식별**하여 효율적으로 갱신하는 데 쓴다.

**조건부 렌더링**
- 조건에 따라 다른 UI를 보여주는 것으로, **삼항 연산자**나 **`&&` 연산자**를 JSX의 `{ }` 안에 사용한다.

**입력 처리**
- `<input>`의 값 변경은 **`onChange`** 이벤트로 처리하고, `event.target.value`로 입력값을 읽어 **state에 저장**한다.

---

## 4장. 렌더링 과정

### 4-1. 렌더링이란?

**비유**: 렌더링은 **그림 그리기**예요. 컴포넌트(설계도)를 보고 화면에 그림을 그리는 일이에요.

컴포넌트는 **순수 함수**여야 해요.

- **순수 함수**: 같은 입력을 넣으면 **항상 같은 출력**이 나오는 함수 (자판기처럼).
- 컴포넌트의 **입력** = props + state
- 컴포넌트의 **출력** = JSX
- 즉 props와 state가 같으면 같은 화면이 나와야 해요.

### 4-2. 렌더링 4단계 (설명 문제 후보)

**비유**: **틀린 그림 찾기**예요. 새 그림과 옛 그림을 비교해서 **바뀐 부분만** 고쳐요.

1. **render**: 컴포넌트 함수를 호출 → JSX를 받아서 **Virtual DOM(가짜 DOM, 초안)**을 만들어요.
2. **비교**: 새 Virtual DOM과 **이전** Virtual DOM을 비교해서 뭐가 바뀌었는지 찾아요.
3. **반영**: 바뀐 부분만 **Real DOM(진짜 DOM)**에 적용해요.
4. **출력**: 브라우저가 바뀐 화면을 보여줘요.

예: `<p>count : 0</p>`이 `<p>count : 1</p>`로 바뀌면, `p`의 텍스트만 0에서 1로 바꿔요.
**비교했는데 바뀐 게 없으면 2단계에서 끝**이에요. (진짜 DOM은 안 건드려요.)

왜 Virtual DOM을 쓸까요? 진짜 DOM을 자꾸 만지는 건 느려서, 가짜로 먼저 비교해서 **꼭 필요한 부분만** 고치려는 거예요.

### 4-3. 렌더링이 일어나는 4가지 경우 (꼭 외우기)

1. **처음 시작할 때**: `root.render()` → 모든 컴포넌트가 한 번 그려져요.
2. **내 state가 바뀔 때**
3. **부모가 렌더링될 때** → 자식도 따라서 그려져요. (props가 같아도!)
4. **쓰고 있는 context 값이 바뀔 때**

> 이 4가지를 알아야 7장(메모이제이션)이 이해돼요.

### 시험 답안용 서술 (그대로 써도 되는 문장)

**렌더링(Rendering)이란?**
- 리액트에서 **컴포넌트 함수를 호출하여 현재 상태에 맞는 UI(JSX)를 만들어 내는 과정**이다.
- 컴포넌트는 **순수 함수**여야 한다. **같은 입력(props, state)에는 항상 같은 출력(JSX)** 을 반환해야 하며, 렌더링 중에 외부 값을 바꾸는 등의 부수 효과를 일으키지 않는다.

**렌더링 과정 4단계**
1. **Render**: 컴포넌트 함수를 호출하여 JSX 결과를 얻고 **Virtual DOM**을 만든다.
2. **비교(Diffing)**: 이전 Virtual DOM과 **비교**하여 **바뀐 부분**을 찾는다.
3. **Commit**: 바뀐 부분**만** **실제 DOM**에 반영한다.
4. 브라우저가 변경된 화면을 **출력**한다.

**Virtual DOM**
- 실제 DOM의 **가벼운 복사본(JavaScript 객체)** 이다. 변경 사항을 Virtual DOM에서 먼저 비교하고 **달라진 부분만 실제 DOM에 반영**하므로 화면 갱신이 **효율적**이다.

**리렌더링이 일어나는 경우 4가지**
1. 최초 렌더링 (`root.render()`)
2. 컴포넌트 **자신의 state가 변경**될 때
3. **부모 컴포넌트가 리렌더링**될 때 (자식도 함께)
4. 사용 중인 **Context의 값이 변경**될 때

---

## 5장. 상태 관리 (useState)

### 5-1. 상태(state)란?

**비유**: **화이트보드**예요.

- 보통 변수(`let a = 0`)는 값을 바꿔도 화면은 모르고 그대로예요.
- **state**는 값이 바뀌면 리액트가 **알아채고 화면을 다시 그려요.**

```jsx
import { useState } from 'react';

const [count, setCount] = useState(0);
```

- `count`: 상태 **변수** (현재 값, 읽기용)
- `setCount`: 상태 **함수** (값을 바꾸는 유일한 방법)
- `0`: 처음 값

흐름: `setCount(5)` → 새 값 저장 → 컴포넌트 함수를 **다시 호출** → 새 JSX → Virtual DOM 비교 → 화면 갱신
(4장 렌더링 과정과 이어져요.)

> **훅(Hook) 규칙**: `useState`, `useEffect` 같은 `use...` 함수는 컴포넌트 함수 **맨 위**에서 호출해요. `if`나 `for` 안에서는 쓰면 안 돼요.

### 5-2. 완성 코드 (통째로 외우기)

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>count : {count}</p>
      <button onClick={() => setCount(count + 1)}>
        +1
      </button>
    </div>
  );
}

export default Counter;
```

### 5-3. 버튼 문법

```jsx
<button onClick={() => setCount(count + 1)}>
<button onClick={() => setCount(prev => prev + 1)}>
<button onClick={handleClick}>
```

- `onClick`은 **낙타표기**예요. (`onclick`이 아니에요.)
- 값 자리에는 **함수**를 넣어요: `() => ...` 또는 함수 이름만 (`handleClick`).

> **자주 하는 실수**
> `onClick={setCount(count + 1)}` → 렌더링 중에 **바로 실행**돼서 무한 반복으로 에러가 나요.
> `onClick={handleClick()}` → 같은 실수예요. 괄호 `()`를 붙이면 안 돼요.

### 5-4. `count + 1` vs `prev =>` (시험에 나올 차이)

**비유**: **ATM 입금**이에요. 통장에 0원이 있고, "1만원 입금"을 두 번 눌러요.

```jsx
setCount(count + 1);
setCount(count + 1);
// 결과: 1 (둘 다 "내가 처음 본 잔액 0"에서 +1)

setCount(prev => prev + 1);
setCount(prev => prev + 1);
// 결과: 2 (매번 "지금 잔액" 기준)
```

- `setCount(count + 1)`: 이번 렌더링에서 **보고 있던 값** 기준으로 계산해요.
- `setCount(prev => prev + 1)`: **가장 최신 값**(prev = previous, 직전 값)을 받아서 계산해요.
- `setCount`는 **예약**이에요. 호출한다고 바로 `count`가 바뀌지 않고, 렌더링이 끝나야 새 값이 보여요.

**prev를 써야 하는 경우**: 연속으로 호출할 때, 값을 계속 쌓을 때, 배열/객체 state를 바꿀 때, `useCallback`의 `[]` 안에서.

### 5-5. 배열/객체 state는 새로 만들어 교체 (1-8장 복습)

```jsx
// 추가
setTodos(prev => [...prev, newTodo]);

// 삭제
setTodos(prev => prev.filter(t => t.id !== id));

// 일부만 수정
setTodos(prev => prev.map(t =>
  t.id === id ? { ...t, done: !t.done } : t
));

// 객체의 일부만 수정
setUser(prev => ({ ...prev, [field]: value }));
```

- 규칙 하나만 기억하세요: **직접 고치지 말고(push 금지) 새로 만들어서 통째로 교체!**
- `map` 안의 삼항 연산자: "내가 찾는 항목이면 바꾼 복사본, 아니면 그대로"

### 시험 답안용 서술 (그대로 써도 되는 문장)

**상태(state)와 useState**
- **상태(state)**: 컴포넌트가 **기억하는 값**으로, **변경되면 컴포넌트가 다시 렌더링**된다. 일반 변수와 달리 렌더링이 반복되어도 **값이 유지**되고, 값이 바뀌면 **화면이 갱신**된다.
- **`useState`**: 함수형 컴포넌트에서 상태를 사용하게 하는 **Hook**이다. `const [state, setState] = useState(초기값);`처럼 **상태 변수와 상태 변경 함수**를 배열로 반환한다.
- 상태는 **반드시 상태 변경 함수(`setState`)로만** 바꿔야 하며, 직접 대입하면 화면이 갱신되지 않는다.

**Hook 규칙**
- Hook은 컴포넌트(또는 커스텀 훅)의 **최상위**에서만 호출하고, **조건문·반복문·중첩 함수 안에서는 호출하지 않는다.**

**상태 변경 함수의 동작**
- `setState`는 **다음 렌더링에 반영될 새 값을 예약**한다. 호출 직후에도 현재 렌더링의 state 값은 **바뀌지 않는다.** 여러 번 호출하면 **일괄 처리(batching)** 된다.
- **함수형 업데이트** `setCount(prev => prev + 1)`: **직전의 최신 상태값(`prev`)** 을 기준으로 새 값을 계산한다. 같은 렌더링에서 여러 번 갱신하거나, 이전 값을 기반으로 계산할 때 사용한다.
- 반면 `setCount(count + 1)`은 **현재 렌더링의 `count`** 를 기준으로 계산한다.

**배열·객체 상태의 갱신 (불변성)**
- 상태가 배열·객체일 때는 **원본을 수정하지 않고** 스프레드 연산자나 `map`, `filter`로 **새로운 값을 만들어** 교체한다. (추가: `[...arr, item]`, 삭제: `filter`, 수정: `map`)

**이벤트 처리**
- 이벤트 핸들러에는 **함수 자체를 전달**한다. (`onClick={() => setCount(count + 1)}`) `onClick={fn()}`처럼 **호출 결과를 전달**하면 렌더링 중에 실행되어 **무한 렌더링**이 발생한다.

---

## 6장. useEffect

### 6-1. 부수효과(side effect)란?

**비유**: 컴포넌트는 **레시피**예요. 같은 재료로 같은 요리를 만드는 게 정상이에요(순수 함수).
그런데 요리 도중에 택배를 주문하거나 밖에 전화(API 호출, 타이머, DOM 직접 조작)를 걸면, 요리와 상관없는 **바깥 세상에 영향**을 주게 돼요. 이걸 **부수효과**라고 해요.

→ 이런 일은 렌더링(레시피) 안에서 하지 말고, **`useEffect` 안으로 분리**해요.

```jsx
useEffect(() => {
  // 부수효과 실행
  return () => {
    // 정리(클린업)
  };
}, [의존성]);
```

### 6-2. 의존성 배열 = "언제 실행할까?"

| 쓰는 모양 | 실행 시점 |
|---|---|
| `useEffect(fn)` | **렌더링할 때마다** |
| `useEffect(fn, [])` | **처음(mount) 한 번만** |
| `useEffect(fn, [x])` | 처음 + **x가 바뀔 때마다** |

- **mount**: 컴포넌트가 처음 화면에 생겨나는 것
- 개발 중(StrictMode)에는 `[]`도 일부러 **2번** 실행될 수 있어요. 버그가 아니에요.

> **자주 하는 실수 (무한 반복)**
> effect 안에서 `setState`를 하는데 의존성을 안 적으면 → 상태 변경 → 렌더링 → effect → 상태 변경... 끝없이 반복돼요.
> 렌더링 중에 `setState`를 직접 부르는 것도 같아요.

### 6-3. 클린업 함수 = "정리하고 가기"

**비유**: 이사 가기 전에 **가스 밸브를 잠그고** 가는 거예요.

- 컴포넌트가 **사라질 때**, 그리고 **다음 effect가 실행되기 직전**에 실행돼요.

타이머 예제 (시작은 `setInterval`, 정지는 `clearInterval`):

```jsx
useEffect(() => {
  const id = setInterval(() => {
    setCount(prev => prev + 1);
  }, 1000);

  return () => clearInterval(id);
}, []);
```

- 1초마다 count를 올려요. 컴포넌트가 사라질 때 타이머를 꺼요. (안 끄면 계속 돌아요.)
- 여기서 `prev =>`를 쓴 이유: `[]`라서 count를 의존성에 안 넣었으니까요.

### 6-4. 비동기 처리와 API 호출

**비유**: **치킨 주문**이에요. 전화로 주문하고(요청) 진동벨(**Promise**)을 받아요. 기다리는 동안 다른 일을 하다가 벨이 울리면(**await**) 받아요.

- **동기**: 한 줄 끝날 때까지 기다렸다가 다음 줄 실행
- **비동기**: 기다리지 않고 다음 일을 진행 (결과는 나중에 받음)
- **async**: 이 함수는 비동기예요 (Promise를 돌려줘요)
- **await**: Promise 결과가 올 때까지 이 줄에서 기다려요
- **Promise 상태 3가지**: Pending(기다리는 중) → Fulfilled(성공) 또는 Rejected(실패)

```jsx
const [users, setUsers] = useState([]);
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);

useEffect(() => {
  const load = async () => {
    try {
      setLoading(true);
      const res = await fetch(url);
      if (!res.ok) throw new Error('실패');
      const data = await res.json();
      setUsers(data);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };
  load();
}, []);
```

**외울 것**
- **상태 3개**: 데이터 / `loading` / `error`
- `useEffect`의 콜백에는 **`async`를 직접 못 붙여요.** → 안에 `async` 함수를 만들고 호출해요.
- `try`(시도) → `catch`(실패 시) → `finally`(성공이든 실패든 마지막에 항상)
- `fetch`는 404, 500 에러에서도 실패로 안 쳐요. → `res.ok`를 **직접 확인**해요.
- `res.json()`: 받은 응답을 JSON 형식으로 읽기

**isCancelled 패턴**

```jsx
let isCancelled = false;
// ... 데이터 받은 후
if (!isCancelled) setUsers(data);

return () => { isCancelled = true; };
```

- 컴포넌트가 사라졌거나 `userId`가 바뀐 뒤에 **늦게 도착한 옛날 응답**이 state를 덮어쓰지 않게 막아요.
- (수업 코드 주석은 "이전 요청 취소"라고 적혀 있지만, 정확히는 요청을 끊는 게 아니라 **결과를 무시**하는 거예요.)

### 시험 답안용 서술 (그대로 써도 되는 문장)

**부수 효과(Side Effect)와 useEffect**
- **부수 효과**: 컴포넌트가 **화면을 그리는 것 외에 수행하는 작업**이다. (API 호출, 타이머 설정, 이벤트 리스너 등록, DOM 직접 접근 등)
- **`useEffect`**: 렌더링이 끝난 뒤에 **부수 효과를 실행**하게 하는 Hook이다. 형식은 `useEffect(() => { 실행할 코드; return () => { 정리 코드 }; }, [의존성 배열]);`

**의존성 배열(Dependency Array)**

| 형태 | 실행 시점 |
|---|---|
| 생략 | **렌더링될 때마다** 실행 |
| `[]` | **처음 렌더링 후 한 번만** 실행 |
| `[x]` | **처음 렌더링 후**, 그리고 **`x`가 바뀔 때마다** 실행 |

**정리(Cleanup) 함수**
- effect가 반환하는 함수로, **컴포넌트가 사라질 때(언마운트)** 와 **다음 effect가 실행되기 직전**에 호출되어 **이전 effect의 작업을 정리**한다. (예: `setInterval`을 `clearInterval`로 해제, 이벤트 리스너 제거)

**비동기 처리**
- **비동기(asynchronous)**: 작업이 끝나기를 기다리지 않고 **다음 코드를 먼저 실행**하는 방식이다. `async` 함수는 **Promise**를 반환하며, `await`는 **Promise의 결과를 기다린다.**
- **Promise 상태**: **Pending**(대기), **Fulfilled**(성공), **Rejected**(실패).
- `useEffect`의 콜백은 **정리 함수 또는 `undefined`만 반환**해야 하는데 `async` 함수는 **Promise를 반환**하므로 **콜백에 `async`를 직접 붙일 수 없다.** → effect 안에 `async` 함수를 **따로 만들어 호출**한다.
- 데이터 요청 상태는 **data, loading, error** 3개의 state로 관리하고, `try-catch-finally`로 오류를 처리한다. `fetch`는 HTTP 오류에도 reject하지 않으므로 **`res.ok`를 확인**한다.

**StrictMode**
- 개발 모드에서 **effect가 두 번 실행**되는 것은 **cleanup이 올바른지 점검**하기 위한 동작이며, 배포 환경에서는 일어나지 않는다.

---

## 7장. 메모이제이션 (memo, useCallback, useMemo)

### 7-1. 왜 필요할까?

4장에서 배운 것: **부모가 렌더링되면 자식도 무조건 렌더링**돼요. 자식이 부모의 값을 안 써도요.

**비유**: 반장이 숙제 검사를 다시 하면, 반 친구 **전원이 숙제를 다시 제출**해야 하는 상황이에요. 이미 낸 사람이 많은데 말이죠.
자식이 가볍다면 상관없지만, **무거운 자식**이라면 낭비예요. 그래서 "안 바뀐 건 기억해 두고 다시 그리지 마!"라고 하는 도구가 메모이제이션(기억)이에요.

### 7-2. 세 가지 도구

| 도구 | 무엇을 기억할까? | 기본 모양 |
|---|---|---|
| `memo` | **컴포넌트** | `memo(컴포넌트)` |
| `useCallback` | **함수** | `useCallback(함수, [의존성])` |
| `useMemo` | **계산한 값** | `useMemo(() => 계산, [의존성])` |

**memo**: "props가 지난번과 같으면 다시 그리지 않을게." (props를 간단히 비교해요.)

```jsx
const Child = memo(({ onClick }) => {
  return <button onClick={onClick}>+1</button>;
});
```

**useMemo**: 오래 걸리는 계산을 매번 다시 하지 않아요. **오답 노트**처럼 이미 푼 답을 적어 두고 재사용해요.

```jsx
const total = useMemo(() => {
  return data.reduce((acc, v) => acc + v, 0);
}, [data]);
```

### 7-3. useCallback이 왜 memo랑 세트일까?

**비유**: 함수는 **레시피 카드**예요.
부모가 다시 렌더링되면, 내용이 똑같은 레시피 카드를 **새로 복사**해서 새 서랍에 넣어요. 내용은 같은데 **서랍 번호(주소)**가 달라져요.
자식은 "어? 서랍 번호가 다르네? 새로운 props가 왔구나!" 하고 다시 그려요. `memo`를 씌워놨어도요.

→ `useCallback`으로 **같은 카드(같은 주소)를 계속 쓰게** 만들어 줘야 `memo`가 효과를 봐요.

```jsx
const Parent = () => {
  const [count, setCount] = useState(0);
  const [text, setText] = useState('');

  const add = useCallback(() => {
    setCount(prev => prev + 1);
  }, []);

  return (
    <>
      <input value={text}
        onChange={e => setText(e.target.value)} />
      <p>{count}</p>
      <Child onClick={add} />
    </>
  );
};
```

- 글자를 입력해서 `text`가 바뀌어도 `Child`는 다시 안 그려져요. (`add`의 주소가 그대로니까)

**외울 것**
- `useCallback`은 **혼자서는 의미가 없어요.** 함수를 props로 받는 자식에 `memo`를 씌워서 **세트로** 써야 해요.
- 반대로 `memo`는 **혼자서도 OK**예요. (props가 함수가 아니라 값이면 되니까)
- `useMemo`는 따로 써요. (오래 걸리는 계산 값 기억)
- 의존성 배열에는 함수나 계산 안에서 **쓰는 state/props를 적어요.**

**의존성 `[]`의 함정**

```jsx
const add = useCallback(() => {
  setCount(count + 1);   // 문제!
}, []);
```

- `[]`라서 함수가 **처음 만들어질 때의 count(0)**에 갇혀요. 버튼을 눌러도 항상 `0 + 1`이라 1에서 멈춰요. (낡은 값에 갇혔다고 해서 stale closure라고 해요.)
- 해결: `setCount(prev => prev + 1)`로 쓰면 count를 읽을 필요가 없어서 `[]`로 안전해요.

> **너무 많이 쓰지 마세요.** 기억하는 데도 메모리가 들고 비교하는 계산도 필요해요.
> 앱이 **느리게 느껴질 때만** 필요한 곳에 쓰는 게 좋아요. (교수님 말씀)

### 시험 답안용 서술 (그대로 써도 되는 문장)

**메모이제이션(Memoization)**
- 이전에 **계산한 결과를 저장해 두었다가**, **같은 입력이 들어오면 다시 계산하지 않고 재사용**하는 최적화 기법이다. 리액트에서는 **불필요한 리렌더링과 재계산을 줄이기 위해** 사용한다.

**종류와 역할**

| 이름 | 대상 | 설명 (답안용) |
|---|---|---|
| `React.memo` | **컴포넌트** | **props가 이전과 같으면** 리렌더링을 **건너뛴다.** (props를 **얕은 비교**) |
| `useCallback` | **함수** | 의존성이 바뀌지 않으면 **같은 함수(같은 주소)** 를 **재사용**한다. |
| `useMemo` | **계산된 값** | 의존성이 바뀌지 않으면 **이전 계산 결과를 재사용**한다. |

- 컴포넌트가 렌더링될 때마다 함수는 **새로 만들어져 주소가 바뀐다.** 그래서 함수를 props로 전달하면 `React.memo`가 "props가 바뀌었다"고 판단하여 **memo의 효과가 사라진다.** 따라서 **`React.memo`와 `useCallback`을 함께** 사용한다.
- `useCallback`, `useMemo`의 **의존성 배열**에 쓰인 값이 바뀌면 새로 만든다. 의존성을 `[]`로 두면 처음 만들어진 시점의 값을 계속 기억하는 **오래된 상태(stale closure)** 문제가 생길 수 있으며, 이때는 **`setState(prev => ...)` 함수형 업데이트**로 해결한다.
- 메모이제이션은 **메모리를 사용하고 코드가 복잡**해지므로, **성능 문제가 있을 때만** 사용한다.

---

## 8장. Context

### 8-1. 문제: props drilling

**비유**: **전달 게임**이에요.
A가 e와 f에게 줄 쪽지가 있는데, 중간 친구(c, d)를 거쳐서만 갈 수 있어요. c와 d는 쪽지가 필요 없는데도 열어보지도 않고 **옆으로 전달만** 해야 해요.

- A → C → D → E 이렇게 **중간 컴포넌트마다 props로 계속 내려주는 것**을 **props drilling**이라고 해요.
- 중간 컴포넌트들이 쓰지도 않는 props를 잔뜩 받게 되고, 계층이 깊어질수록 복잡해져요.

### 8-2. 해결: Context (공유 게시판)

**비유**: 교실 **게시판**이에요. 쪽지를 전달하지 않고 게시판에 붙여 놓으면, 필요한 친구가 **직접 가서 읽어요.**

게시판을 쓰려면 **3가지**가 필요해요 (외우기!):

1. **`createContext()`**: 빈 **게시판을 만들어요.** (컴포넌트 **바깥**에서)
2. **`Provider`**: 게시판에 **글을 올리는 사람(공급자)**. `value`에 값을 담아요.
3. **`useContext()`**: 게시판에서 **글을 읽는 사람(소비자)**.

```jsx
// ThemeContext.jsx
import { createContext } from 'react';
export const ThemeContext = createContext();
```

```jsx
// 공급자: 상태를 가진 부모
import { ThemeContext } from './ThemeContext';

const ContextBasic = () => {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <ThemeButton />
    </ThemeContext.Provider>
  );
};
```

```jsx
// 소비자: Provider 아래에 있는 컴포넌트
import { useContext } from 'react';

const ThemeButton = () => {
  const { theme, setTheme } = useContext(ThemeContext);
  return (
    <button onClick={() =>
      setTheme(prev => prev === 'light' ? 'dark' : 'light')}>
      현재 테마 : {theme}
    </button>
  );
};
```

**외울 것**
- `Provider`로 감싼 **하위 컴포넌트 전체**(자식, 손자, 증손자)가 값을 쓸 수 있어요.
- `value={{ theme, setTheme }}`: 바깥 `{ }`는 JS 시작, 안쪽 `{ }`는 **객체**예요. 값 두 개를 한꺼번에 보내요.
- `useContext(ThemeContext)` 괄호 안에는 **내가 읽을 context**를 반드시 써요.
- 필요한 것만 꺼내도 돼요: `const { theme } = useContext(...)`.
- **context 값이 바뀌면** 그 context를 쓰는 **모든 컴포넌트가 다시 렌더링**돼요. (4장 4번)
- Provider 밖에서 `useContext`를 쓰면 값이 `undefined`라서, 구조분해하면 에러가 나요.

### 8-3. Multi Context: 게시판을 나눠요

**비유**: 게시판 **한 개**에 "학급 공지"와 "급식 메뉴"를 다 붙여놨다고 해볼게요. 급식 메뉴만 바뀌어도 학급 공지만 보던 친구까지 **전부 다시 확인**해야 해요.
→ 서로 관계없는 데이터는 **게시판을 따로** 만들어요. 필요한 것만 읽으니까 렌더링이 줄어요.

- **데이터 성격별로 context를 분리**해요 (예: `UserContext`, `ThemeContext`).
- 여러 컴포넌트가 쓰니까 context는 **별도 파일**로 만들어 `export`하고, 쓰는 곳에서 `import`해요.
- Provider를 **겹쳐서** 써요.

```jsx
<UserContext.Provider value={{ user, setUser }}>
  <ThemeContext.Provider value={{ theme, setTheme }}>
    <UserProfile />
  </ThemeContext.Provider>
</UserContext.Provider>
```

### 8-4. 커스텀 Provider와 children

Provider가 많아지면 겹겹이 쌓여서 지저분해져요. 하나의 컴포넌트로 **묶어서 정리**해요.

```jsx
const MyContextProvider = ({ children }) => {
  const [user, setUser] = useState({ name: 'Kim' });
  const [theme, setTheme] = useState('light');
  return (
    <UserContext.Provider value={{ user, setUser }}>
      <ThemeContext.Provider value={{ theme, setTheme }}>
        {children}
      </ThemeContext.Provider>
    </UserContext.Provider>
  );
};
```

```jsx
const ContextMulti = () => {
  return (
    <>
      <Header />
      <MyContextProvider>
        <UserProfile />
      </MyContextProvider>
    </>
  );
};
```

**children이란?** 태그 **사이에 끼워 넣은 내용물**이에요. **샌드위치**를 생각하세요. 빵(`MyContextProvider`) 사이에 속재료(`<UserProfile />`)를 넣으면, 그 속재료가 `children`으로 들어와요.

- 이렇게 나누면 `Header`는 context와 상관없는 부분, `UserProfile`은 context를 쓰는 부분이라는 걸 **구조만 봐도 알 수 있어요.**
- (바로 아래 8-5: context 값이 바뀔 때 생기는 불필요한 렌더링을 `useMemo`로 줄이는 방법)

### 8-5. Context + useMemo (불필요한 렌더링 줄이기)

**문제**: Provider의 `value`에 `{ theme, setTheme }`처럼 객체를 **그 자리에서 만들면**, 부모가 렌더링될 때마다 **새 객체(새 주소)** 가 만들어져요. 내용이 똑같아도 **주소가 바뀌면 "value가 바뀌었다"** 고 판단해서, 그 context를 쓰는 컴포넌트가 **전부 다시 렌더링**돼요.

- **비유**: 내용물이 똑같은 택배인데 **송장번호(주소)만 매번 새로 붙으면**, 받는 사람이 "새 택배네?" 하고 매번 다시 뜯어봐요.
- 예: `user`가 바뀌어서 `MyContextProvider`가 다시 렌더링되면, `theme` 객체도 새로 만들어져요. 값은 그대로인데 theme을 쓰는 컴포넌트가 또 렌더링돼요.

**해결**: `useMemo`로 value를 **기억**해서 주소가 안 바뀌게 해요. (아래는 실습 코드)

```jsx
const MyContextProvider = ({ children }) => {
  const [user, setUser] = useState({
    name: 'Bob Lee', role: 'Admin', email: 'bob@ok.com'
  });
  const [theme, setTheme] = useState('light');

  // theme 데이터를 기억하는 useMemo 적용
  const themeValue = useMemo(
    () => ({ theme, setTheme }), [theme]
  );

  return (
    <UserContext.Provider value={{ user, setUser }}>
      <ThemeContext.Provider value={themeValue}>
        {children}
      </ThemeContext.Provider>
    </UserContext.Provider>
  );
};
```

- `useMemo(함수, [의존성])`: 함수가 돌려준 **결과값**을 기억해요. `[theme]`이 바뀔 때만 다시 계산해요.
- `Provider value={themeValue}`: 기억된 객체를 그대로 넘겨요. `user`만 바뀌면 `themeValue`는 **같은 주소**라서 theme 쓰는 컴포넌트는 렌더링 안 해요.
- **언제 쓰나?** ① value가 객체라서 매번 새로 만들어질 때 ② value가 **계산이 복잡해서** 매번 만들기 부담될 때.

> 내 레포 `ContextMulti.jsx`를 보면 `value={{ themeValue }}`로 한 겹 더 감싸져 있어요. 이러면 받는 쪽의 `{ theme, setTheme }`이 `undefined`가 돼요. **`value={themeValue}`** 가 맞아요. (수정 후 커밋 필요)

### 시험 답안용 서술 (그대로 써도 되는 문장)

**Props Drilling과 Context**
- **Props Drilling**: 깊이 있는 자식 컴포넌트에 데이터를 전달하기 위해, **중간 컴포넌트들이 쓰지 않는 props를 계속 전달**해야 하는 문제이다. 코드가 복잡해지고 유지보수가 어렵다.
- **Context API**: 컴포넌트 트리 **전역에서 데이터를 공유**하게 해주어, **props를 일일이 전달하지 않고** 필요한 컴포넌트가 직접 값을 사용할 수 있게 한다. (예: 로그인 사용자, 테마)

**사용 3단계**
1. **생성**: `const MyContext = createContext();`
2. **제공**: `<MyContext.Provider value={값}> ... </MyContext.Provider>` 로 하위 컴포넌트에 값을 **공급**한다.
3. **사용**: 하위 컴포넌트에서 `const 값 = useContext(MyContext);` 로 **값을 읽는다.**

**동작 특징**
- Provider의 **`value`가 바뀌면**, 그 Context를 **`useContext`로 사용하는 컴포넌트는 모두 리렌더링**된다.
- 여러 종류의 값을 공유할 때는 **Context를 여러 개** 만들어 Provider를 **중첩**(Multi Context)하고, 이를 하나의 **커스텀 Provider 컴포넌트**로 묶어 `children`을 감싸게 하면 관리하기 쉽다.

**Context와 useMemo**
- Provider의 `value`가 객체이면 **부모가 렌더링될 때마다 새 객체(새 주소)** 가 만들어져, 값이 같아도 **value가 바뀐 것으로 인식**되어 그 context를 사용하는 컴포넌트가 불필요하게 **리렌더링**된다.
- 이를 막기 위해 **`useMemo`로 value를 기억**(메모이제이션)하여 **의존성이 바뀔 때만** 새로 만들게 한다. 값을 만드는 **계산이 복잡한 경우**에도 `useContext`와 `useMemo`를 함께 사용한다.
- 또한 context를 **여러 개로 나누면**, 각 컴포넌트가 필요한 context만 사용하므로 불필요한 렌더링을 줄일 수 있다.

---

## 9장. useRef

### 9-1. 일반 변수 / 상태변수 / ref 변수

- **일반 변수**: 컴포넌트는 함수라서 **렌더링할 때마다 처음부터 다시 실행**돼요. 그래서 `let num = 1; num++`은 값을 올려도 **다시 1로 초기화**돼요. 값이 유지되지 않아요.
- **상태변수(`useState`)**: 값이 **유지**돼요. 대신 바뀌면 **무조건 렌더링**을 일으켜요. (화면에 안 보여주는 값이어도 마찬가지)
- **ref 변수(`useRef`)**: 값이 **유지**되는데 **바뀌어도 렌더링을 일으키지 않아요.** "화면에 보여줄 값은 아니고, 내부에서만 기억하고 싶은 값"에 써요.

**비유**: 화면과 상관없는 **개인 서랍**이에요. 값을 넣고 빼도 화면은 다시 안 그려지고, 컴포넌트가 다시 그려져도 서랍 속 물건은 그대로예요.

| | 일반 변수 | 상태변수 | ref 변수 |
|---|---|---|---|
| 렌더링 후 값 유지 | X (초기화) | O | O |
| 값이 바뀌면 렌더링 | 일으키지 않음 | **일으킴** | **일으키지 않음** |
| 값 바꾸는 방법 | 직접 대입 | **set 함수** | **`ref.current`에 직접 대입** |
| 화면 출력 | 가능 | 가능 | 가능 |

### 9-2. 만드는 법

```jsx
const ref = useRef(1);   // 초기값은 숫자, 문자열, 배열, 객체 뭐든 가능
```

- `ref`는 **객체**로 만들어져요: `{ current: 1 }` (속성이 `current` 하나, 값이 초기값)
- 값을 바꿀 때: `ref.current = 2;` (set 함수 없이 **직접 대입**. 렌더링 안 일어남)
- 값을 읽을 때: `ref.current`

### 9-3. useRef를 쓰는 3가지 경우 (외우기)

1. **내부 값 기억**: 렌더링을 일으키지 않고 값 유지 (예: 이전 값)
2. **DOM 요소 접근**: 입력창 등 **실제 DOM 요소를 가리키는 포인터**
3. **타이머 보관**: `setInterval`이 돌려주는 **타이머 id** 저장

### 9-4. 예제 ① 이전 값 기억 (RefBasic)

```jsx
export default function RefBasic() {
  const [count, setCount] = useState(0);
  const countRef = useRef(null);

  useEffect(() => {
    countRef.current = count;
  }, [count]);

  return (
    <div>
      <h1>현재 값 : {count}</h1>
      <h1>이전 값 : {countRef.current}</h1>
      <button onClick={() => setCount(count - 1)}>감소</button>
      <button onClick={() => setCount(count + 1)}>증가</button>
    </div>
  );
}
```

**왜 "이전 값"이 나올까? (동작 순서)**
1. 버튼을 눌러 `count`가 1 → 2로 바뀌어요.
2. **렌더링 시작**: 화면에 `count`는 2, `countRef.current`는 **아직 1**이라 이전 값 1이 출력돼요.
3. **렌더링이 끝난 뒤** `useEffect`가 실행되어 `countRef.current = 2`로 갱신돼요. (ref는 바뀌어도 렌더링을 안 일으켜서 화면은 그대로)
4. 다음 렌더링 때 그 값이 "이전 값"으로 보여요.

- `useEffect`를 안 쓰고 렌더링 중에 `countRef.current = count`를 하면 현재 값과 똑같아져서 이전 값을 못 얻어요.

### 9-5. 예제 ② DOM 요소 접근 (RefInput)

```jsx
export default function RefInput() {
  const [keyword, setKeyword] = useState("");
  const [history, setHistory] = useState([]);
  const inputRef = useRef(null);  // 입력창을 가리킬 ref
  const countRef = useRef(0);     // 검색 횟수 보관

  const handleSearch = () => {
    const value = keyword.trim();
    if (value == "") {
      alert("검색어를 입력하세요!!");
      inputRef.current.focus();   // 입력창으로 포커스
      return;
    }
    setHistory(prev => [...prev, value]);
    countRef.current++;           // 렌더링 없이 횟수 증가
    setKeyword("");
    inputRef.current.focus();
  };

  return (
    <div>
      <input type="text" placeholder="검색어 입력..."
        ref={inputRef}
        value={keyword}
        onChange={e => setKeyword(e.target.value)} />
      <button onClick={handleSearch}>Search</button>
      <ul>
        {history.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}
```

- **`ref={inputRef}`가 핵심**이에요. 이렇게 쓰면 React가 **그 `<input>`의 실제 DOM 요소를 찾아서 `inputRef.current`에 넣어 줘요.** 그래서 `inputRef.current.focus()`로 입력창을 직접 조작할 수 있어요.
- 일반 JavaScript에서 `const t = document.getElementById("title");`로 DOM 요소를 변수에 담는 것과 **같은 역할**이에요. (`t`가 요소를 가리키는 포인터)
- `countRef`는 검색 횟수라서 화면에 안 보여줘도 되니 **렌더링을 일으키지 않는 ref**가 적당해요.

### 9-6. 예제 ③ 타이머 id 보관 (RefTimer)

```jsx
export default function RefTimer() {
  const [seconds, setSeconds] = useState(0);
  const timerRef = useRef(null);  // 타이머 id를 가리키는 ref

  const startTimer = () => {
    if (timerRef.current != null) return;  // 이미 동작 중이면 끝
    timerRef.current = setInterval(() => {
      setSeconds(prev => prev + 1);
    }, 1000);
  };

  const stopTimer = () => {
    clearInterval(timerRef.current);
    timerRef.current = null;
  };

  const resetTimer = () => {
    stopTimer();
    setSeconds(0);
  };

  // 컴포넌트가 삭제될 때 타이머 정리 (Clean Up)
  useEffect(() => {
    return () => {
      clearInterval(timerRef.current);
    };
  }, []);

  return (
    <div>
      <h3>{seconds} 초</h3>
      <button onClick={startTimer}>Start</button>
      <button onClick={stopTimer}>Stop</button>
      <button onClick={resetTimer}>Reset</button>
    </div>
  );
}
```

**왜 타이머 id를 ref에 넣을까?**
- `seconds`가 바뀔 때마다 **렌더링이 계속 일어나요.** 타이머 id가 일반 변수면 렌더링 때 **초기화**되어 이전 타이머를 잃어버리고 **타이머가 중복**으로 만들어져요.
- 렌더링해도 **값이 유지**되고, id를 저장한다고 **렌더링을 일으킬 필요는 없으니** ref가 딱 맞아요.
- `setSeconds(prev => prev + 1)`: 1초마다 **연속으로** 값을 바꾸므로 `prev` 방식으로 써요. (5장 복습)
- **클린업**: 컴포넌트가 사라질 때 `clearInterval`로 타이머를 정리해요. 안 하면 사라진 컴포넌트에서 타이머가 계속 돌아요.

### 시험 답안용 서술 (그대로 써도 되는 문장)

**useRef**
- **`useRef`는 렌더링 사이에 값을 유지하면서, 값이 바뀌어도 렌더링을 일으키지 않는 ref 변수를 만드는 Hook이다.** 반환값은 `{ current: 초기값 }` 형태의 객체이며, 값은 `ref.current`에 **직접 대입**하여 변경한다.
- **상태변수와의 차이**: 둘 다 렌더링 사이에 값이 유지된다. 그러나 **상태변수는 값이 바뀌면 리렌더링을 일으키고 set 함수로 변경**하지만, **ref 변수는 리렌더링을 일으키지 않고 `current`에 직접 대입하여 변경**한다.
- **사용 경우 3가지**: ① **렌더링을 일으키지 않고 내부 값을 기억**할 때 ② **DOM 요소에 접근**할 때(`ref` 속성에 연결) ③ **타이머 id를 보관**할 때

**DOM 접근**
- DOM 요소에 접근하려면 `const inputRef = useRef(null);`로 ref를 만들고 요소의 **`ref={inputRef}`** 속성에 연결한다. 그러면 **`inputRef.current`가 해당 DOM 요소를 가리키며**, `inputRef.current.focus()`처럼 호출할 수 있다.

### 외울 것

- `const ref = useRef(초기값);` → `{ current: 초기값 }`
- 변경은 `ref.current = 값;` (**set 함수 없음, 렌더링 안 일어남**)
- DOM 연결: `<input ref={inputRef} />` → `inputRef.current.focus()`
- 용도 3가지: 값 기억 / DOM 접근 / 타이머 id

### 자주 하는 실수

- `ref = 2`처럼 쓰는 것 → **`ref.current = 2`** 여야 해요.
- ref 값을 바꿨는데 **화면이 안 바뀐다고** 당황하는 것 → ref는 **렌더링을 일으키지 않아요.** 화면에 바로 반영해야 하는 값이면 상태변수를 써요.
- 화면에 보여줘야 하는 값을 ref로 만드는 것 → 상태변수로 만들어요.
- 타이머 id를 일반 변수에 저장해서 **타이머가 중복**되는 것 → ref에 저장해요.

---

## 10장. useReducer

### 10-1. 왜 필요할까? (useState 복습과 문제점)

`useState`는 **상태변수**와 그것을 바꾸는 **변경함수(set)** 한 쌍이에요.

- `setPoint(point + 1)`은 `point`를 직접 고치는 게 아니에요. **상태변수는 immutable(변경 불가)** 이라서, 계산한 새 값 `2`를 **새 메모리에 만들고**, `point`가 가리키는 **주소를 새 값으로 바꿔요.** (값을 직접 바꾸는 `point = point + 1`은 React에서 안 돼요. → 5장)
- 버튼을 누르면 이벤트 핸들러(`handlePoint`)가 변경함수를 호출해요: 버튼 `onClick` → **핸들러** → `setPoint(...)` → 상태 변경
- **문제**: 상태를 바꾸는 방법(+10, -10, 초기화 ...)이 늘어날수록 **핸들러 함수가 계속 늘어나요.** 상태가 책(제목, 가격, 출판사, 발간일...)처럼 **복잡한 객체**면 더 심해져서, 코드가 길어지고 **가독성과 유지보수**가 나빠져요.

**해결**: `useReducer`. 상태를 바꾸는 **모든 방법을 reducer 함수 하나에 모아요.**

**비유**: **은행 창구**예요. 손님(버튼)이 **주문서(action)** 를 내면(dispatch), 창구 직원(reducer)이 **주문서 종류에 따라** 규칙대로 처리해서 **새 상태**를 만들어줘요. 직원은 한 명이고, 처리 방법이 한곳에 모여 있어요.

### 10-2. 구조

```jsx
const [state, dispatch] = useReducer(reducer, 초기상태);
```

| 이름 | 역할 |
|---|---|
| `state` | **상태변수.** `초기상태`로 만들어져요. (이름은 마음대로) |
| `reducer` | 상태를 바꾸는 **모든 기능이 모인 함수.** `(state, action)`을 받아 **새 상태를 반환** |
| `action` | 어떤 기능인지 알려주는 **객체** (`{ type: 'ADD' }`) |
| `dispatch` | reducer를 **호출해주는 함수.** 이벤트 핸들러 자리에서 호출. (이름은 관례적으로 `dispatch`) |

`useState`와 비교하면 **`set` 함수 자리에 `reducer`가 있고**, `set`을 부르는 대신 **`dispatch(action)`** 을 불러요.

**동작 흐름 (외우기)**
1. 사용자가 버튼을 누르거나 입력해요. (이벤트 발생)
2. **`dispatch(action)`** 호출
3. dispatch가 **현재 state와 action을 reducer에 전달**해서 실행
4. reducer가 `action.type`에 맞는 case에서 **새 상태를 반환**
5. 반환된 값이 **state가 되고**, state가 바뀌었으니 **리렌더링**

### 10-3. 예제 ① 카운터 (ReducerBasic)

**reducer 함수**: 매개변수는 `(state, action)` **두 개로 정해져 있어요.** 함수 이름은 마음대로예요.

```jsx
function numberReducer(state, action) {
  switch (action.type) {
    case 'ADD':
      return { count: state.count + 1,
               startTime: new Date().toString() };
    case 'SUB':
      return { count: state.count - 1,
               startTime: state.startTime };
    case 'RESET':
      return { count: 0,
               startTime: new Date().toString() };
    case 'TIMES':
      return { count: state.count * action.payload[0],
               startTime: new Date().toString() };
    default:
      throw new Error('액션 종류가 정의되지 않았습니다.');
  }
}
```

- `action.type`으로 **switch** 해서 종류별로 처리해요. 각 case는 **새 상태 객체를 return**해요. (return이 있으니 `break`는 필요 없어요.)
- 액션 type은 **관습적으로 대문자**로 써요. (꼭 대문자일 필요는 없어요)
- **`SUB`처럼 바꾸지 않는 값은 `state.startTime`으로 그대로 가져가요.** 이걸 빼먹으면 그 속성이 **사라져요.** (수업에서 시간이 사라졌던 이유)
- **default**: 정의 안 된 action이 오면 ① `return state;`(현재 상태 그대로) 하거나 ② `throw new Error(...)`로 **dispatch를 호출한 쪽에 예외를 전달**해요. 둘 중 원하는 방식을 쓰면 돼요.

**초기상태가 복잡할 때: 초기화 함수**

```jsx
function initState(num) {
  return {
    count: num,
    startTime: new Date().toString()
  };
}
```

**컴포넌트: 상태변수와 dispatch 생성**

```jsx
export default function ReducerBasic() {
  // 초기상태를 직접 줄 때
  // const [state, dispatch] = useReducer(numberReducer, { count: 0 });

  // 초기화 함수를 쓸 때
  const [state, dispatch] = useReducer(numberReducer, 5, initState);

  return (
    <div>
      <h1>useReducer 예제</h1>
      <h2>Number : {state.count}</h2>
      <h3>Date : {state.startTime}</h3>
      <button onClick={() => dispatch({ type: 'ADD' })}>ADD</button>
      <button onClick={() => dispatch({ type: 'SUB' })}>SUB</button>
      <button onClick={() => dispatch({ type: 'RESET' })}>RESET</button>
      <button onClick={() =>
        dispatch({ type: 'TIMES', payload: [2, 4, 6] })
      }>TIMES</button>
    </div>
  );
}
```

- **`useReducer(numberReducer, 5, initState)`**: **세 번째 인자가 초기화 함수**예요. 두 번째 인자 `5`가 **`initState(num)`의 `num`으로 들어가서** `{ count: 5, startTime: 현재시간 }`이 초기 state가 돼요.
- **state가 객체**라서 `state.count`, `state.startTime`으로 꺼내 써요. (초기상태를 `0`으로 주면 state는 숫자, `{ count: 0 }`으로 주면 객체)
- `onClick={() => dispatch({ type: 'ADD' })}`: **dispatch가 이벤트 핸들러 역할**이에요. 버튼마다 **다른 type**을 보내서 구별해요.

**payload (추가로 전달하는 값)**
- `TIMES`는 "얼마를 곱할지" 추가 값이 필요해요. 그 값을 **action 객체의 `payload` 속성**에 담아요: `{ type: 'TIMES', payload: 2 }`
- payload는 **관례적인 이름**이에요. (다른 이름도 가능하지만 다들 payload라고 써요)
- 값이 여러 개면 **배열**(`payload[0]`)이나 **객체**(`payload.속성`)로 담으면 어떤 형태든 전달할 수 있어요.

### 10-4. 예제 ② 객체 상태 (ReducerUser)

```jsx
function reducer(state, action) {
  switch (action.type) {
    case 'CHANGE_NAME':
      return { ...state, name: action.payload };
    case 'ADD_AGE':
      return { ...state, age: state.age + action.payload };
    default:
      return state;
  }
}

const initialState = { name: 'Tommy', age: 22 };

export default function ReducerUser() {
  const [user, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <h1>회원 정보 관리</h1>
      <p>이름 : {user.name}</p>
      <p>나이 : {user.age}</p>
      <input type="text" value={user.name}
        onChange={e => dispatch({
          type: 'CHANGE_NAME',
          payload: e.target.value
        })} />
      <button onClick={() => dispatch({
        type: 'ADD_AGE', payload: 2
      })}>ADD</button>
    </div>
  );
}
```

- **`{ ...state, name: action.payload }`**: 현재 state를 **스프레드로 복사**하고 `name`만 **덮어써서** 새 객체를 만들어요. (1-7장, 불변성) 원본 `state`를 직접 고치지 않아요.
- 입력창은 `onChange`에서 **useState의 `setName(e.target.value)` 대신** `dispatch({ type, payload: e.target.value })`를 써요.
- `ADD_AGE`: 현재 나이에 payload만큼 더해요. (`state.age + action.payload`)
- 상태변수 이름(`state`, `user`)은 **마음대로** 정해도 되지만, `dispatch`는 관례적으로 이 이름을 써요.
- 상태가 복잡한 객체이고(예: 장바구니 배열), 추가/삭제/수량 변경 같은 **여러 기능**이 필요할수록 reducer가 유리해요. (장바구니 예제는 시험 범위 밖)

### 시험 답안용 서술 (그대로 써도 되는 문장)

**useReducer**
- **`useReducer`는 상태를 변경하는 모든 로직을 reducer 함수 하나에 모아서 관리하는 Hook이다.** 상태가 복잡하거나 상태를 변경하는 방법이 다양할 때, `useState`처럼 핸들러 함수가 여러 개로 흩어지는 문제를 해결한다.
- **형식**: `const [state, dispatch] = useReducer(reducer, 초기상태);`
  - **state**: 상태변수
  - **reducer**: **현재 상태(state)와 액션(action)을 받아 새로운 상태를 반환**하는 함수. `action.type`에 따라 `switch`로 처리한다.
  - **action**: 상태를 어떻게 변경할지 나타내는 **객체**(`type`과, 필요하면 `payload`)
  - **dispatch**: **action을 reducer에 전달하여 reducer를 호출**하는 함수

**동작 과정**
- 이벤트가 발생하면 **`dispatch(action)`을 호출**한다 → dispatch가 **현재 state와 action을 reducer에 전달**한다 → reducer가 **action.type에 맞는 새 상태를 반환**한다 → 반환된 값으로 **state가 변경되고 리렌더링**된다.

**useState와의 차이**
- `useState`는 변경함수(set)를 이벤트 핸들러에서 직접 호출하며, 변경 방법이 많아지면 핸들러가 늘어난다. `useReducer`는 **변경 로직을 reducer 한 곳에 모으고 dispatch로 호출**하므로 복잡한 상태 관리에 적합하다.

**payload**
- **payload는 액션을 처리하기 위해 추가로 전달하는 값**으로, action 객체의 속성으로 담는다. 여러 값은 배열이나 객체로 전달한다.

**상태변수의 불변성(immutable)**
- 상태변수는 **직접 값을 변경할 수 없다.** 변경함수는 **새로운 값을 새 메모리에 만들고, 상태변수가 가리키는 주소를 그 새 값으로 바꾼다.** 따라서 객체·배열 상태는 **스프레드 연산자로 복사한 새 값**으로 교체해야 한다.

### 외울 것

- `const [state, dispatch] = useReducer(reducer, 초기상태);`
- reducer 매개변수: **`(state, action)`**, `switch (action.type)`, 각 case는 **새 상태를 return**
- 버튼: `onClick={() => dispatch({ type: 'ADD' })}`
- 추가 값: `dispatch({ type: 'TIMES', payload: 2 })` → `action.payload`
- 입력창: `onChange={e => dispatch({ type: 'CHANGE_NAME', payload: e.target.value })}`
- 객체 상태 변경: `return { ...state, name: action.payload };`
- 초기화 함수: `useReducer(reducer, 5, initState)` (5가 `initState`의 매개변수로)
- default: `return state;` 또는 `throw new Error(...)`

### 자주 하는 실수

- `onClick={dispatch({ type: 'ADD' })}`처럼 쓰는 것 → **호출 결과**가 들어가서 렌더링 때 바로 실행돼요. **`() =>`** 로 감싸야 해요.
- reducer에서 `state.count++`처럼 **state를 직접 고치는 것** → 새 객체를 **return**해야 해요.
- 일부 속성만 return 해서 **나머지 속성이 사라지는 것** → `...state`로 복사하거나 `startTime: state.startTime`처럼 그대로 가져가요.
- action의 `type` 철자가 reducer의 case와 **다른 것** → 처리되지 않거나 에러가 나요. (대소문자도 구별)
- `dispatch`에 `type`이 아니라 값만 보내는 것 → **action은 객체**여야 해요.
- `ReducerUser.jsx`의 `default: break;`는 `undefined`를 반환해서 정의 안 된 action이 오면 **state가 사라져요.** → `default: return state;`로 고치세요. (내 레포 수정 필요)

---

## 11장. 백지 연습문제

**방법**: 정답(다음 장)을 가리고, 백지에 먼저 써보세요. 막히면 해당 장을 다시 읽으세요.

1. `[1, 2, 3, 4, 5]`의 각 값에 1을 더한 새 배열을 `map`으로 쓰세요.
2. 같은 배열에서 짝수만 `filter`로 뽑으세요.
3. `a = [1, 2, 3]`의 끝에 4를 추가한 **새 배열**을 만드는 코드 (원본을 고치지 말고).
4. 객체 `user`의 `age`만 21로 바꾼 복사본 코드.
5. `count`를 1 올리는 버튼 (값을 직접 쓰는 방식, `prev` 방식 두 가지).
6. `setCount(count + 1)`을 두 번 쓴 결과와, `prev =>`로 두 번 쓴 결과가 다른 이유를 설명하세요.
7. `useEffect`의 의존성 배열 3가지 형태(생략 / `[]` / `[x]`)가 각각 언제 실행되는지 쓰세요.
8. 컴포넌트가 렌더링되는 **4가지 경우**를 쓰세요.
9. `memo`, `useCallback`, `useMemo`가 각각 **무엇을 기억**하는지, 그리고 `useCallback`과 `memo`를 **같이 쓰는 이유**를 쓰세요.
10. props drilling이란 무엇이고, context를 쓰는 **3단계**를 코드로 쓰세요.
11. 순수 함수란? 렌더링 **4단계**를 쓰세요.
12. 1초마다 count가 올라가는 타이머를 `useEffect`로 쓰세요. (정리까지)
13. `useRef`로 만든 변수의 **형태**와 **값을 바꾸는 방법**, 상태변수와의 **차이**를 쓰세요.
14. `useRef`를 쓰는 **3가지 경우**를 쓰세요.
15. 입력창(`<input>`)을 `inputRef`로 가리키고, 버튼을 누르면 입력창에 **포커스**가 가게 하는 코드를 쓰세요.
16. 타이머 id를 `ref`에 저장하는 이유를 쓰세요. (일반 변수와 비교)
17. Context의 `value`와 함께 **`useMemo`를 쓰는 이유**를 쓰세요. (코드도)
18. `useReducer`의 **형식**을 쓰고, `state` / `reducer` / `action` / `dispatch`가 각각 무엇인지 쓰세요.
19. `useReducer`의 **동작 과정**을 순서대로 쓰세요. (버튼 클릭부터 리렌더링까지)
20. `count`를 다루는 reducer를 쓰세요. (`ADD`: +1, `SUB`: -1, `RESET`: 0, 정의 안 된 action은 에러) 그리고 **ADD 버튼**의 `dispatch` 구문을 쓰세요.
21. `TIMES` 액션으로 `count`에 **payload만큼 곱하는** case와, 그 **버튼 구문**(payload 3)을 쓰세요.
22. 객체 state `{ name, age }`에서 **입력창으로 이름을 바꾸는** reducer case와 `input`의 `onChange` 구문을 쓰세요.
23. 상태변수가 **immutable(변경 불가)** 하다는 것의 의미를 설명하세요.
24. `useReducer`의 **초기화 함수**를 쓰는 이유와, `5`를 넘겨 `{ count: 5 }`로 초기화하는 코드를 쓰세요.

---

## 정답

1. `const b = a.map(v => v + 1);` → `[2, 3, 4, 5, 6]`
2. `const c = a.filter(v => v % 2 === 0);` → `[2, 4]`
3. `const b = [...a, 4];`
4. `const u2 = { ...user, age: 21 };`
5. 값 직접: `<button onClick={() => setCount(count + 1)}>`
   prev: `<button onClick={() => setCount(prev => prev + 1)}>`
6. `count + 1`은 두 번 다 **이번 렌더링에서 본 같은 count**를 기준으로 계산해서 결과가 +1이에요. `prev =>`는 **직전에 계산된 최신 값**을 기준으로 해서 +2가 돼요.
7. 생략: 렌더링할 때마다 / `[]`: 처음 한 번만 / `[x]`: 처음 + x가 바뀔 때마다
8. ① 처음 `root.render()` ② 자기 state 변경 ③ 부모가 렌더링 ④ 사용 중인 context 값 변경
9. `memo`=컴포넌트, `useCallback`=함수, `useMemo`=계산한 값.
   함수는 렌더링마다 새로 만들어져 주소가 바뀌는데, 이걸 props로 넘기면 자식이 "props가 바뀌었다"고 판단해서 `memo`가 소용없어져요. `useCallback`으로 함수 주소를 유지해야 `memo`가 효과가 있어요.
10. 부모의 값을 쓰지도 않는 중간 컴포넌트들을 거쳐 props로 계속 내려주는 것.
    ① `const MyContext = createContext();`
    ② `<MyContext.Provider value={{ ... }}> ... </MyContext.Provider>`
    ③ `const { ... } = useContext(MyContext);`
11. 순수 함수: 같은 입력이면 항상 같은 출력. (컴포넌트의 입력은 props와 state, 출력은 JSX)
    ① render(컴포넌트 호출, JSX, Virtual DOM 생성) ② 이전 Virtual DOM과 비교 ③ 바뀐 부분만 Real DOM에 반영 ④ 화면 출력
12. 아래 코드.

```jsx
useEffect(() => {
  const id = setInterval(() => {
    setCount(prev => prev + 1);
  }, 1000);

  return () => clearInterval(id);
}, []);
```

13. `useRef(초기값)`은 **`{ current: 초기값 }` 객체**를 만들어요. 값은 **`ref.current = 값`으로 직접 대입**해서 바꾸고 **렌더링을 일으키지 않아요.** 상태변수는 **set 함수로 바꾸고, 바뀌면 렌더링**을 일으켜요. (둘 다 렌더링 사이에 값은 유지)
14. ① 렌더링 없이 **내부 값 기억** ② **DOM 요소 접근** ③ **타이머 id 보관**
15. 아래 코드.
16. 타이머 id가 **일반 변수**면 렌더링 때 **초기화**돼서 이전 타이머를 잃고 **중복 타이머**가 생겨요. ref는 **렌더링해도 값이 유지**되고, id를 저장한다고 **렌더링을 일으키지도 않아요.**
17. value가 객체면 **부모가 렌더링될 때마다 새 객체(새 주소)** 가 만들어져서, 내용이 같아도 context를 쓰는 컴포넌트가 **불필요하게 리렌더링**돼요. `useMemo`로 **기억해서 주소를 유지**하고, **의존성이 바뀔 때만** 새로 만들어요. (계산이 복잡한 값일 때도 사용)
18. `const [state, dispatch] = useReducer(reducer, 초기상태);` **state**=상태변수 / **reducer**=`(state, action)`을 받아 **새 상태를 반환**하는 함수 / **action**=변경 종류를 나타내는 **객체** / **dispatch**=action을 reducer에 전달해 **reducer를 호출**하는 함수
19. ① 버튼 클릭 등 이벤트 ② `dispatch(action)` 호출 ③ 현재 state와 action이 **reducer에 전달**됨 ④ `action.type`에 맞는 case가 **새 상태를 반환** ⑤ **state 변경, 리렌더링**
20. 아래 코드.
21. 아래 코드.
22. 아래 코드.
23. 상태변수는 **값을 직접 바꿀 수 없어요.** 변경함수는 **새 값을 새 메모리에 만들고, 상태변수가 가리키는 주소를 새 값으로 바꿔요.** (`point = point + 1`처럼 직접 대입은 안 됨) 그래서 객체·배열은 **스프레드로 복사한 새 값**으로 교체해야 해요.
24. 초기상태를 **계산해서 만들어야 할 때** 함수로 정의해요. 세 번째 인자로 넘기면 두 번째 인자가 그 함수의 매개변수로 들어가요.

```jsx
// 15
const inputRef = useRef(null);
<input type="text" ref={inputRef} />
<button onClick={() => inputRef.current.focus()}>포커스</button>

// 20 (reducer)
function reducer(state, action) {
  switch (action.type) {
    case 'ADD':   return { count: state.count + 1 };
    case 'SUB':   return { count: state.count - 1 };
    case 'RESET': return { count: 0 };
    default:
      throw new Error('액션 종류가 정의되지 않았습니다.');
  }
}
// 20 (버튼)
<button onClick={() => dispatch({ type: 'ADD' })}>ADD</button>

// 21
case 'TIMES':
  return { count: state.count * action.payload };
<button onClick={() =>
  dispatch({ type: 'TIMES', payload: 3 })}>TIMES</button>

// 22
case 'CHANGE_NAME':
  return { ...state, name: action.payload };
<input value={user.name}
  onChange={e => dispatch({
    type: 'CHANGE_NAME',
    payload: e.target.value
  })} />

// 24
function initState(num) {
  return { count: num };
}
const [state, dispatch] = useReducer(reducer, 5, initState);
```

---

## 시험 전 체크리스트

- [ ] map, filter, forEach, reduce의 차이를 말할 수 있다
- [ ] 스프레드(`...`)로 배열/객체를 새로 만들 수 있다
- [ ] 웹이 화면을 만드는 과정(파싱, DOM Tree, CSS Tree, Render Tree)을 설명할 수 있다
- [ ] MPA/SSR과 SPA/CSR의 차이를 설명할 수 있다
- [ ] JSX 규칙 3가지를 쓸 수 있다
- [ ] `useState` 카운터 코드를 백지에 쓸 수 있다
- [ ] `count + 1`과 `prev =>`의 차이를 설명할 수 있다
- [ ] 렌더링 4단계와 렌더링 발생 4가지 경우를 쓸 수 있다
- [ ] useEffect 의존성 배열 3가지와 클린업을 설명할 수 있다
- [ ] 비동기 fetch 패턴(상태 3개, try/catch/finally)을 쓸 수 있다
- [ ] memo / useCallback / useMemo를 구별하고 세트인 이유를 말할 수 있다
- [ ] props drilling과 Context 3단계를 코드로 쓸 수 있다
- [ ] Context의 value에 `useMemo`를 같이 쓰는 이유를 말할 수 있다
- [ ] 일반 변수 / 상태변수 / ref 변수의 차이를 설명할 수 있다
- [ ] `useRef` 3가지 용도와 `ref={inputRef}` → `inputRef.current.focus()`를 쓸 수 있다
- [ ] `useReducer` 형식과 state / reducer / action / dispatch를 설명할 수 있다
- [ ] 카운터 reducer(ADD, SUB, RESET)와 dispatch 버튼 구문을 백지에 쓸 수 있다
- [ ] payload와 객체 상태(`{ ...state, name: action.payload }`)를 쓸 수 있다
- [ ] 상태변수가 immutable하다는 의미를 설명할 수 있다