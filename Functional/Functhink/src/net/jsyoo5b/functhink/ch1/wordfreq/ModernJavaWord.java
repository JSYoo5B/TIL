package net.jsyoo5b.functhink.ch1.wordfreq;

import com.sun.istack.NotNull;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ModernJavaWord extends Word {
    @NotNull
    private List<String> regexToList(String words, String regex) {
        List<String> wordList = new ArrayList<>();
        Matcher m = Pattern.compile(regex).matcher(words);
        while(m.find())
            wordList.add(m.group());
        return wordList;
    }

    @Override
    public Map<String, Integer> wordFreq(String words) {
        // TreeMap will store word and it's frequency <Word, FreqCnt>
        TreeMap<String, Integer> wordMap = new TreeMap<String, Integer>();
        regexToList(words, "\\w+").stream()
                .map(w -> w.toLowerCase())              // change all word token to lower cases
                .filter(w -> !NON_WORDS.contains(w))    // filter the word token which doesn't included in NON_WORDS
                .forEach(w -> wordMap.put(w, wordMap.getOrDefault(w, 0) + 1));
        return wordMap;
    }
}
