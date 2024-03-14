class Record {
  public int count;
  public int nextIndex;
  public Record(int count, int nextIndex) {
    this.count = count;
    this.nextIndex = nextIndex;
  }
};

class Solution {
  public int getMaxRepetitions(String s1, int n1, String s2, int n2) {
    // [count(s1 matches s2[i..n)), next index of s2[i..n)]
    List<Record> records = new ArrayList<>();

    for (int i = 0; i < s2.length(); ++i) {
      int count = 0;
      int nextIndex = i;
      for (int j = 0; j < s1.length(); ++j)
        if (s2.charAt(nextIndex) == s1.charAt(j))
          if (++nextIndex == s2.length()) { // There's a match.
            ++count;
            nextIndex = 0;
          }
      records.add(new Record(count, nextIndex));
    }

    int matches = 0; // `s1` matches `s2`.
    int index = 0;

    while (n1-- > 0) {
      matches += records.get(index).count;
      index = records.get(index).nextIndex;
    }

    return matches / n2; // `s1` matches `s2`.
  }
}