package net.jsyoo5b.functhink.ch1.wordfreq;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Words {
    // List-up non-words (articles, conjunctions, contraction followings, etc.)
    private static final Set<String> NON_WORDS = new HashSet<String>() {{
        add("the"); add("and"); add("of");  add("to");  add("a");
        add("i");   add("it");  add("in");  add("or");  add("is");
        add("d"); add("s"); add("as");  add("so");  add("but");
        add("be");
    }};

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
