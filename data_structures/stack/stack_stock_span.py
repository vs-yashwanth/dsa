from stack import StackRaw


def stock_span_brute(stocks):  # O(n^2)
    spans = []
    i = 0
    n = len(stocks)
    while i < n:
        span = 1
        j = i-1
        while j >= 0 and stocks[j] <= stocks[i]:
            span += 1
            j -= 1

        spans.append(span)
        i += 1
    return spans


def stock_span_stack(stocks):  # O(n), O(n)
    stack = StackRaw()
    stack.push(0)
    spans = [1]
    for i in range(1, len(stocks)):
        while not stack.is_empty() and stocks[i] >= stocks[stack.peek()]:
            stack.pop()
        spans.append(i+1 if stack.is_empty() else i-stack.peek())
        stack.push(i)
    return spans


if __name__ == '__main__':

    stock_span = stock_span_stack

    print(stock_span([10, 20, 30, 40, 50]))
    # Spans: [1, 2, 3, 4, 5]

    print(stock_span([50, 40, 30, 20, 10]))
    # Spans: [1, 1, 1, 1, 1]

    print(stock_span([100, 80, 90, 60, 70, 75, 85]))
    # Spans: [1, 1, 2, 1, 2, 3, 4]
