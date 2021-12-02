# MapReduce

- Map과 Reduce 연산을 조합하여 클러스터에서 실행, 큰 데이터를 처리
- 이를 구현한 오픈소스 프로젝트인 Hadoop MapReduce

**단점**

- Map의 입출력 및 Reduce의 입출력을 매번 HDFS에 쓰고 읽는다 
→ 느리다
- MapReduce 코드는 작성하기 불편하다.

🛠️ **Workflow**

- HDFS 디스크에서 파일을 읽고 계산 후 중간 결과를 `디스크`에 write 하는 과정을 반복

[디스크와 파티션 개념](https://www.notion.so/fd7e52aed3ec4040aaa9eb42b204630f)

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb49a325c-bbb8-4ce7-958f-fff3bd9a8948%2FUntitled.png?table=block&id=8a677650-b021-4b4b-9692-43cdd8adb756&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1540&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

# Apache Spark

- 핵심 개념: RDD (Resilient Distributed Dataset)
    - 탄력적으로 분산된 데이터셋
    - 하나의 거대한 가상의 리스트를 마치 로컬에 있는 작은 리스트처럼  다룰 수 있게 해주는 개념
    - 데이터를 어떻게 구해낼지를 표현하는 Transformation을 기술한 Lineage(계보)를 interactive하게 만들어 낸 후 Action을 통해 lazy하게 값을 구해냄
    
- 인터페이스: Scala

🛠️ **Workflow**

- spark에서는 중간 결과들이 `디스크` 가 아닌 `메모리` 로 대체
- 쿼리할 때 마다 처음부터 읽어오기보다는 한번 램에 올려놓고 그 다음에 쿼리쿼리쿼리!

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F1bba4b7f-e484-4eee-a0aa-fcf38bc90ed3%2FUntitled.png?table=block&id=a4e7e1c4-4375-4bdd-8e22-02359afb6575&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1540&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

### Hadoop MapReduce → Spark

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F9c688a85-bf8f-4b83-9b98-a4e4554b639d%2FUntitled.png?table=block&id=722efcd4-8781-432b-ac62-865886164742&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1540&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

**Map Reduce**

어떤 Work이 있을때 Master는 그 Work을 분할하여 Slaves(여러 대의 서버)에 나눠주고, 서버는 그 일을 처리하여 다시 서버로 보내서 Map과 Reduce를 반복한다.

Java로만 되어있고 Batch processing 작업이 `Hadoop file system` 이라고 불리는 `hdfs` 에서 진행되다 보니 느리다.

*💡 Idea*

> MR이 iteration에서 빡센 이유는 각 iteration을 돌 때마다 스테이지간 자료공유가 HDFS를 거치기 때문이지 않을까? 그걸 넘쳐나는 `RAM`으로 하자!
> 

*⚠️ Problem*

> 중간에 뽀개지면(fault) 어떡하지? 램은 빠르지만 깨지기 쉬울 수 있다.
> 

*💡 Idea*

> RAM도 ROM처럼 read-only로만 써볼까? 이것이 RDD!
> 

**RDD**

- 한 번 데이터가 만들어지만 수정되지 않음 (read-only)
- 부모로부터 어떻게 만들어졌는지 계보(lineage)만 기록해도 fault-tolerant
- lineage계보를 `DAG` (directed acyclic graph)로 디자인

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbd1dca55-bc66-4adb-8993-059aef83eff0%2FUntitled.png?table=block&id=93069432-d44d-456a-a923-904968069628&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1540&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

> 어떻게 만들어지는지 계보를 다 그려놓은 상태에서 즉 대강의 Execution Plan이 다 만들어진 상태에서 뒤에 실행하므로 자원이 배치된, 배치될 상황을 미리 고려해서 최적의 코스로 돌 수 있다.
> 

**Spark**

기본적으로 Scala로 구현되어있고 Batch만이 아니라 실시간, 반복적, 대화형 그래프에도 사용가능하다. ⇒ ***다목적***

하둡보다 compact하고 쉬운데, 데이터를 메모리에서 캐싱해서 처리하기 때문에 빠르다.

❓ Databricks

- spark을 만든 개발자들이 차린 회사
- spark기반의 data anaytics platform을 만든다.

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F60a5b734-9187-45a5-9ca9-268129a2ddce%2FUntitled.png?table=block&id=882371c5-2a86-4205-b239-941b7fdd4dcc&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1540&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

- spark 은 자동차 엔진 , databricks는 자동차 한대로 비유할 수 있겠다.

## RDD, DataFrame, Dataset

- 스파크 v1에서 발표한 RDD의 단점을 개선한 것이 스파크 v2에서 발표한 Dataset과 DataFrame

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc160c0b4-fda6-4bdb-a147-efb7d7461e55%2FUntitled.png?table=block&id=69a1bc69-0849-4824-b5e8-f0abf7ccde56&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1540&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

- 스파크 2.0에서 데이터 프레임과 데이터셋을 통합
- 스칼라 API에서 Dataset[Row]는 DataFrame을 의미

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3f51bbc8-e2c6-4b8b-8492-ee2eb87e4436%2FUntitled.png?table=block&id=0c6cf3d5-d3b5-42d3-9e1e-11c99256ebdb&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1540&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

🛠️ Spark Application 개발 시

- RDD는 스파크 컨텍스트(SparkContext)를 이용
- 데이터셋, 데이터프레임은 스파크 세션(SparkSession) 객체를 이용

## 데이터 저장

> DataFrame과 Dataset을 이용하여 데이터를 저장하고 불러오기
> 

### 압축 포맷 지정

`option` : gzip, snappy 등의 형식 이용 가능

```bash
// snappy 형식 압축 
peopleDS.select("name").write.format("json").option("compression", "snappy").save("/user/ds_1")
```

### 저장 모드(SaveMode)

`mode` : 파일을 덮어쓸 것인지, 이어쓸 것인지 설정

| 설정 | 비고 |
| --- | --- |
| saveMode.ErrorlfExist | 파일이 있으면 에러 처리 |
| SaveMode.Append | 다른 이름으로 파일 추가 |
| SaveMode.Overwrite | 기존 파일을 삭제하고 추가 |
| SaveMode.Ignore | 파일이 있으면 저장하지 않고, 에러 처리도 하지 않음 |

## 스파크 설정

### 메모리, 코어 설정

| spark.driver.memory | 2g | 드라이버가 사용할 메모리 |
| --- | --- | --- |
| spark.executor.memory | 5g | 익스큐터가 사용할 메모리 |
| spark.executor.cores | 1 | 애플리케이션에 사용할 코어 개수 |
| spark.executor.extraLibraryPath | /opt/hadoop/lib/native | 드라이버가 사용할 추가 라이브러리 |
| spark.driver.extraJavaOptions | Djava.library.path=/opt/hadoop/lib/native | 드라이버의 자바 옵션 |
| spark.driver.extraLibraryPath | /opt/hadoop/lib/native | 드라이버가 사용할 추가 라이브러리 |
- 설정값 확인 시에는 `get` 을 이용spark.conf.get("spark.master")

# 스파크 구조

1. 드라이버 : 작업을 관리
2. 클러스터 매니저 : 작업이 실행되는 노드를 관리

## 스파크 애플리케이션

- `마스터-슬레이브` 구조
- 작업을 관장하는 `Driver` 와 실제작업이 동작하는 `Executor` 로 구성

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fae469ab7-129a-4e2b-95d9-21a55e713a15%2FUntitled.png?table=block&id=b11ee20a-cba4-4b9d-8133-dceaebc4262a&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1540&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

### Driver

- Driver는 SparkContext객체를 생성
- 클러스터 매니저와 통신하면서 클러스터의 자원 관리를 지원
- 애플리케이션의 라이프 사이클 관리
- 사용자로부터 입력을 받아서 애플리케이션에 전달하고 작업 처리 결과를 사용자에게 알려줌

### Executor

- Task 실행을 담당하는 에이전트로 실제 작업을 진행하는 프로세스
- 1개의 Excutor = 1개의 YARN 컨테이너
- 1개의 Task = 1개의 core
- 하나의 excutor가 여러개의 task를 동시 실행 가능

| 설정 | 기본값 | 비고 |
| --- | --- | --- |
| spark.executor.instances | 1 | 익스큐터 개수 |
| spark.executor.memory | 512m | 익스큐터가 사용할 메모리 |
| spark.executor.extraJavaOptions | JVM 옵션 |  |
| spark.yarn.executor.memoryOverhead | 0.07 | 메모리 오버헤드 비율 |
| spark.executor.cores | 1 | 애플리케이션에 사용할 코어 개수 |

### Task

- Executor에서 실행되는 실제 작업
- Cache를 공유하여 작업의 속도를 높임

🛠️ **작업 구성**

1. 잡 (Job)
    - 스파크 애플리케이션으로 제출된 작업
2. 스테이지 (Stage)
    - 잡을 작업의 단위에 따라 구분한 것
3. 태스크 (Task)
    - Executor에서 실행되는 실제 작업
    - 데이터를 읽거나 필터링

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F95b9b9c3-8d3f-4fa5-a760-b6a505ace2f6%2FUntitled.png?table=block&id=1735f5ca-3efe-474d-afe8-ef3ce5b1e6e6&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1540&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

## 클러스터 매니저

스파크는 여러가지 클러스터 매니저를 지원

- YARN
    - 하둡 클러스터 매니저
    - 리소스 매니저, 노드 매니저로 구성 됨
- Mesos
    - 동적 리소스 공유 및 격리를 사용하여 여러 소스의 워크로드를 처리
    - 아파치의 클러스터 매니저
    - 마스터와 슬레이브로 구성됨
- StandAlone
    - 스파크에서 자체적으로 제공하는 클러스터 매니저
    - 각 노드에서 하나의 익스큐터만 실행 가능