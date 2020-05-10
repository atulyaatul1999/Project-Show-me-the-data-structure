import sys
import random

dic = {}
tem = []
fr = []
rootheap = ""

class MinHeapNode:
    def setNode(self, left, right, freq, char):
        self.left = left
        self.right = right
        self.freq = freq
        self.char = char
        return self


def huffmanCoding(arr, freq):
    heapArr = []

    for i in range(len(arr)):
        heapArr.append(MinHeapNode().setNode(None, None, freq[i], arr[i]))

    while (len(heapArr) > 1):
        left = heapArr.pop(0)
        right = heapArr.pop(0)
        insertionSort(heapArr, MinHeapNode().setNode(left, right, left.freq + right.freq, left.char + right.char))

    rootheap = heapArr.pop()

    return rootheap


def printHeap(heap, str):
    if heap.left != None:
        printHeap(heap.left, str + '0')

    if heap.right != None:
        printHeap(heap.right, str + '1')

    if heap.left == None:
        dic[heap.char] = str


def insertionSort(heapArr, heap):
    index = len(heapArr)
    for i in range(len(heapArr)):
        if heap.freq < heapArr[i].freq:
            index = i
            break
    heapArr.insert(index, heap)


def endcoding(str):
    strval = ''
    for i in range(len(str)):
        strval = strval + dic[str[i]]

    return strval


def huffmandecode(rootheap, strvalencoded):
    index = 0;
    orgstr = '';

    while index < len(strvalencoded):
        str = getchar(rootheap, index, strvalencoded)
        index = index + len(dic[str])
        orgstr = orgstr + str
    return orgstr


def getchar(rootheap, index, strvalencoded):
    if rootheap.left == None:
        return rootheap.char

    number = int(strvalencoded[index])
    if number == 0:
        return getchar(rootheap.left, index + 1, strvalencoded)

    if number == 1:
        return getchar(rootheap.right, index + 1, strvalencoded)


def huffman_encoding(data):
    l = len(data)
    for i in range(0, l):
        s1 = data[i].lower()
        flag = 0
        for j in tem:
            if j.lower() == s1:
                flag = 1
        if flag == 0:
            tem.append(s1)
            c = 0
            for j in range(0, l):
                if data[j].lower() == s1:
                    c = c + 1
            fr.append(c)
    rootheap = huffmanCoding(tem, fr)
    printHeap(rootheap, '')
    strvalencoded = endcoding(data)
    return strvalencoded, rootheap


def huffman_decoding(data, tree):
    orgencoded = huffmandecode(tree, data)
    return orgencoded

def show_result(a_great_sentence):
    if len(a_great_sentence)==0:
        print("the sentence is empty , it can't be compressed!")
    else:
        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "the bird is the word"
    show_result(a_great_sentence)
    #here the final output we get our input string "the bird is the word"

    a_great_sentence = ""
    show_result(a_great_sentence)
    #here the final output we get our input string "-?;'"

    a_great_sentence = "aaaaaaaa"
    show_result(a_great_sentence)
    # here the final output we get our input string "-this is new word/"