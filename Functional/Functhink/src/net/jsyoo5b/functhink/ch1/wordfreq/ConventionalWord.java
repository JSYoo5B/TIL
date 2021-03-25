package net.jsyoo5b.functhink.ch1.wordfreq;

import java.util.Map;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ConventionalWord extends Word{

    @Override
    public Map<String, Integer> wordFreq(String words) {
        // TreeMap will store word and it's frequency <Word, FreqCnt>
        TreeMap<String, Integer> wordMap = new TreeMap<String, Integer>();
        // Use Regex to find all words (alphabet groups)
        Matcher m = Pattern.compile("\\w+").matcher(words);

        while(m.find()) {
            String word = m.group().toLowerCase();
            if (! NON_WORDS.contains(word)) {
                if (wordMap.get(word) == null) {
                    // When the word weren't counted, add to entry
                    wordMap.put(word, 1);
                }
                else {
                    // Otherwise, increase the count
                    wordMap.put(word, wordMap.get(word) + 1);
                }

                // TIP: if-else code block above can be shorten by:
                //  wordMap.merge(word, 1, Integer::sum);
            }
        }

        return wordMap;
    }
}
