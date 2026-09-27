## 큰 그림 (계층 구조)
Node.js  → JavaScript를 브라우저 없이 실행 가능하게 하는 기반 환경
Vite     → 리액트 프로젝트 뼈대 생성 + 개발 서버 실행 도구
React    → 화면(UI)을 만드는 JavaScript 라이브러리 (프론트엔드 전용)
JSX      → React를 사용할 때, 화면 구조를 코드 안에 표현하는 문법

## JavaScript와 Node.js
- JavaScript는 원래 브라우저 안에서 화면을 동작시키는(프론트엔드) 용도로 탄생한 언어. Java와는 이름만 비슷할 뿐 별개의 언어.
- Node.js는 브라우저 없이 컴퓨터에서 독립적으로 JavaScript를 실행할 수 있게 해주는 프로그램. 이 덕분에 JavaScript로 서버(백엔드) 개발도 가능해짐.

## React가 뭔가
웹 화면(UI)을 만드는 JavaScript 라이브러리. 화면을 작은 조각(컴포넌트)으로 나눠서 조립하는 방식.

## 핵심 용어
- **Node.js**: JavaScript를 브라우저 밖(컴퓨터)에서 실행할 수 있게 해주는 프로그램. 리액트 개발의 기반.
- **npm**: Node.js용 패키지 관리자. 남이 만든 라이브러리를 설치/관리 (Python의 pip 같은 역할).
- **npx**: 설치 없이 도구를 일회성으로 실행. 새 프로젝트 만들 때 주로 사용.
- **Vite**: 리액트 프로젝트를 빠르게 생성/실행해주는 빌드 도구. `npm create vite@latest` 명령으로 새 프로젝트 시작.
- **JSX**: React를 사용할 때, JavaScript 코드 안에서 `<h1></h1>` 같은 HTML 스타일 태그를 그대로 쓸 수 있게 해주는 문법. `.jsx` 확장자. 브라우저는 JSX를 직접 이해하지 못하므로, Vite가 순수 JavaScript로 변환(트랜스파일)해줌.
- **컴포넌트(Component)**: 화면의 한 조각(예: 버튼, 카드, 헤더)을 함수 하나로 표현한 것.

## State (useState)
- `const [값, set값함수] = useState(초기값)` 형태로 사용
- 일반 변수와 달리, state가 바뀌면 화면이 자동으로 다시 그려짐 (리렌더링)
- state는 props로 자식 컴포넌트에 전달 가능 (값과 변경 함수 둘 다)

## state 업데이트 시 주의점
- 같은 렌더링 안에서 setState를 여러 번 연속 호출할 때, `setX(x + 1)` 형태는 누적되지 않음 (매번 같은 이전 값을 참조)
- `setX(prev => prev + 1)` 형태를 쓰면 이전 값을 기준으로 정확히 누적됨

## 배열/객체 State와 불변성
- state가 배열/객체일 때, 원본을 직접 수정(push, 필드 직접 대입 등)하면 리액트가 변화를 감지 못해 화면이 갱신되지 않을 수 있음
- 항상 스프레드 연산자(`...`)로 기존 내용을 복사한 "새로운 배열/객체"를 만들어 교체해야 함
  - 배열에 추가: `setArr(prev => [...prev, 새값])`
  - 배열 항목 일부 수정: `setArr(prev => prev.map(item => 조건 ? {...item, 필드: 새값} : item))`
  - 배열 항목 삭제: `setArr(prev => prev.filter(item => 조건))`
  - 객체 필드 수정: `setObj(prev => ({...prev, 필드: 새값}))`

## 동적 필드명 (computed property name)
- `{ [변수]: 값 }` 형태로, 변수의 값을 객체의 키 이름으로 사용 가능
- 하나의 함수로 여러 필드를 처리할 때 유용 (예: `updateUser(field, value)`)

## 이벤트 핸들러 작성 시
- `onChange={(e) => handleFunc(e)}` 처럼 이벤트 객체(e)를 매개변수로 명시하는 것이 안전 (전역 event 객체 직접 참조는 지양)

## 개발 서버란
`npm run dev`로 실행되는 서버는 "내 컴퓨터 안에서만 도는 임시 미리보기 서버"이지, 여러 사람이 접속하는 진짜 서비스 서버가 아님. 진짜 서비스를 위해선 별도로 서버(데이터베이스, 보안 포함)를 구축해야 함.

## 프로젝트 실행 흐름 (Vite 기준)
1. `npm create vite@latest 프로젝트명` → 새 프로젝트 생성
2. `cd 프로젝트명` → 폴더 이동
3. `npm install` → 필요한 라이브러리 설치 (node_modules 생성)
4. `npm run dev` → 개발 서버 실행, 브라우저에서 확인

## 헷갈렸던 점
- Vite와 Eclipse는 무관함 (Vite=리액트/VS Code, Eclipse=JSP)
- JSX는 "개발 환경"이 아니라 React를 쓸 때의 "문법"일 뿐임
- React는 기본적으로 프론트엔드 전용 (백엔드는 별도 도구 필요)
- 이벤트 핸들러 작성 시 `onChange={(e) => handleFunc(e)}`처럼 이벤트 객체(e)를 매개변수로 명시하는 게 안전함 (전역 event 객체 직접 참조는 지양)