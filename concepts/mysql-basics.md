# MySQL 기초

## 접속 도구 3가지 (모두 같은 MySQL 서버에 접속하는 클라이언트)
- 커맨드라인 클라이언트(`mysql`): `mysql -u root -p`로 접속, SQL 직접 입력 (SQL 문은 `;`로 끝냄)
  - `show databases;`, `use DB명;`, `show tables;`, `desc 테이블명;`
- MySQL Shell(`mysqlsh`): 커맨드라인의 확장판, SQL/JavaScript/Python 모드 지원 (`\sql`, `\js`, `\py`로 전환)
- MySQL Workbench: GUI 도구, 쿼리 작성·실행, 테이블 구조 확인/편집, ER 다이어그램
- JSP 등 애플리케이션은 JDBC로 접속하는 또 하나의 클라이언트