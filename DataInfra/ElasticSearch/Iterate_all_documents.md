# 전체 코드

```python
def iterate_all_documents(es, index, logger, pagesize=250, scroll_timeout="15m", **kwargs):
        """
        Helper to iterate ALL values from a single index
        Yields all the documents.
        """
        is_first = True
        while True:
            # Scroll next
            try:
                if is_first:  # Initialize scroll
                    result = es.search(index=index, scroll=scroll_timeout, **kwargs, body={
                        "size": pagesize
                    })
                    is_first = False
                else:
                    result = es.scroll(body={
                        "scroll_id": scroll_id,
                        "scroll": scroll_timeout
                    })
            except NotFoundError as nfe:
                # Exit conditions
                # NotFoundError: NotFoundError(404, 'search_phase_execution_exception',
                #   'No search context found for id [262012]')
                # NotFoundError: NotFoundError(404, '{"succeeded":true,"num_freed":0}')
                logger.warning(f'{nfe.status_code}, {nfe.error}')
                if nfe.status_code == 404:
                    is_first = True
            finally:
                scroll_id = result["_scroll_id"]
                hits = result["hits"]["hits"]
                # Stop after no more docs
                if not hits:
                    logger.info(f"scorll_id={scroll_id} is successfully closed.")
                    break
            # Yield each entry
            yield from (hit['_source'] for hit in hits)
```

# Size 매개변수

위의 코드에서는 함수에 pagesize 를 250으로 주고 해당 인자를 size 매개변수에 전달하고있다.

[elastic search 가이드](https://www.elastic.co/guide/en/elasticsearch/reference/current/paginate-search-results.html)에 따르면 size변수는 **요청하고자하는 document의 개수**이다.

# Scroll 매개변수

elasticsearch의 scroll는 자주 바뀌는 데이터에 따라 질의 결과가 달라지는 것을 방지하고 검색 시간 기준으로의 데이터를검색하는데 사용한다. 대신 단점은 메모리에 정보가 저장된다. search context 라는 정보로 메모리에 저장된다. 

scroll 매개 변수는 search context를 활성 상태로 유지해야 하는 기간을 Elastic Search에 알려준다. 따라서 이 정보가 계속 남아 있게 되면 메모리 부족을 일으킬 수 있다. 그래서 이런 정보가 너무 메모리에 남아 있지 않게 하기 위해 scroll timeout을 줄 수 있다.

하지만 scroll timeout을 너무 짧게 주었을 때 스크롤 데이터의 배치가 반환되기에 시간이충분하지 않을 수 있기 때문에 log를 찍어보면서 적절한 시간을 파악한 후 설정해 주면 되겠다.

## NotFoundError(404, 'search_phase_execution_exception', 'No search context found for id [262012]')

NotFoundError는 위에서 말한 것 처럼, scroll timeout 시간을 너무 짧게 설정해서 timeout exception이 발생했을 때 그 결과로써 나타날 수 있다.

위의 코드에서는 scroll timeout을 1m으로 설정하였는데, 나 같은 경우에는 document를 긁어올때마다 해당 데이터로 전처리 작업을 수행하는 시간이 매우 길어서 404에러가 발생했다.

### 해결

```
2021-12-04 17:52:48,833 0th Document's Anchor Extract Start!
/data1/home/hy.jin/git/inkling/src/inkling/wiki/extract_anchor.py:251: DeprecationWarning: The 'body' parameter is deprecated for the 'search' API and will be removed in a future version. Instead use API parameters directly. See https://github.com/elastic/elasticsearch-py/issues/1698 for more information
  res = self.es_client.search(
/data1/home/hy.jin/.pyenv/versions/hypy38/lib/python3.8/site-packages/tunip/es_utils.py:19: DeprecationWarning: The 'body' parameter is deprecated for the 'scroll' API and will be removed in a future version. Instead use API parameters directly. See https://github.com/elastic/elasticsearch-py/issues/1698 for more information
  result = es.scroll(body={
2021-12-04 18:16:04,854 404, search_phase_execution_exception
21/12/04 18:16:20 WARN shortcircuit.DomainSocketFactory: The short-circuit local reads feature cannot be used because libhadoop cannot be loaded.
21/12/04 18:16:21 WARN scheduler.TaskSetManager: Stage 0 contains a task of very large size (3974 KiB). The maximum recommended task size is 1000 KiB.

[Stage 0:>                                                          (0 + 1) / 1]

                                                                                
2021-12-04 18:16:23,117 DataFrame Row Count: 10000
2021-12-04 18:16:23,118 1 write complete!
```

처음 scorll timeout은 15분이었고, 5시 52분에 scroll을 시작하고 6시 16분에 전처리된 데이터를 spark에 쓰는 중 404에러가 발생했기 때문에 timeout을 넉넉하게 30m으로  수정해주었다.

그 결과 더 이상 NotFoundError가 발생하지 않았다! 

# Reference.

[https://techoverflow.net/2019/05/07/elasticsearch-how-to-iterate-scroll-through-all-documents-in-index/](https://techoverflow.net/2019/05/07/elasticsearch-how-to-iterate-scroll-through-all-documents-in-index/)

[https://knight76.tistory.com/entry/elasticsearch-scroll-scroll-timeout-scroll-관련-팁](https://knight76.tistory.com/entry/elasticsearch-scroll-scroll-timeout-scroll-%EA%B4%80%EB%A0%A8-%ED%8C%81)