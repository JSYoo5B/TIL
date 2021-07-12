package net.jsyoo5b.functhink.ch1.wordfreq;

import java.util.*;

public class Word {
    // List-up non-words (articles, conjunctions, contraction followings, etc.)
    protected static final Set<String> NON_WORDS = new HashSet<String>() {{
        add("the"); add("and"); add("of");  add("to");  add("a");
        add("i");   add("it");  add("in");  add("or");  add("is");
        add("d"); add("s"); add("as");  add("so");  add("but");
        add("be");
    }};

    public Map<String, Integer> wordFreq(String words) {
        throw new UnsupportedOperationException("Not implemented");
    }
}
