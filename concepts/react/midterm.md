# 스크립트프로그래밍 중간고사 쉬운 정리

> **시험** 10/22(목) 15:30 · A-411 예정(교수님이 재공지) · 범위는 10/19(월) 수업까지
> **형태** 수업 예제 중심. 문법을 **외워서 직접 쓰는** 문제 (예: "map으로 배열을 바꾸는 코드를 쓰시오")

**이 문서 읽는 법**
각 장은 이 순서예요: 비유(쉬운 그림) → 개념 → 코드 → 외울 것 → 자주 하는 실수.
코드는 눈으로만 보지 말고, 장마다 **백지에 직접 써보세요.** 시험이 "쓰는 문제"라서요.

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
| 9 | useRef, useReducer | 예습 (수업 후 보강) |
| 10 | 백지 연습문제 + 정답 | 최종 점검 |

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
- (다음 수업 예고: context 값이 바뀔 때 생기는 불필요한 렌더링을 `useMemo`로 줄이는 방법)

---

## 9장. useRef, useReducer (예습)

**아직 수업 전이에요.** 10/19 수업을 듣고 필기로 바꿔주세요. 수업 내용과 다를 수 있어요.

### useRef = 렌더링을 안 일으키는 보관함

- **비유**: 화면과 상관없는 **서랍**이에요. 값을 넣고 빼도 화면은 다시 안 그려져요.
- DOM 요소를 직접 잡을 때도 써요 (`ref: DOM 사용하기`).

```jsx
const inputRef = useRef(null);

<input ref={inputRef} />
<button onClick={() => inputRef.current.focus()}>
  입력창으로 이동
</button>
```

- 값은 `.current`에 들어 있어요.

### useReducer = 은행 창구

- **비유**: 손님이 **주문서(action)**를 내면, 창구 직원(**reducer**)이 규칙대로 처리해서 새 상태를 만들어요.
- useState로 상태 바꾸는 코드가 여기저기 흩어지면, 한곳에 모아서 관리해요.

```jsx
function reducer(state, action) {
  switch (action.type) {
    case 'inc':
      return { count: state.count + 1 };
    default:
      return state;
  }
}

const [state, dispatch] = useReducer(
  reducer, { count: 0 }
);

dispatch({ type: 'inc' });   // 주문서 제출
```

---

## 10장. 백지 연습문제

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
- [ ] (10/19 수업 후) useRef, useReducer 필기 추가
