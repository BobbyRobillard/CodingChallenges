package CodingChallenges.Searching.Graphs.BreadthFirstSearch;

import java.util.ArrayList;
import java.util.HashMap;

public class BFS {
    public HashMap<Integer, ArrayList<Integer>> edgesToGraph(int[] edges) {
        HashMap<Integer, ArrayList<Integer>> graph = new HashMap<Integer, ArrayList<Integer>>();
        for(int i=0; i<edges.length; i++) {
            if(edges[i] != -1) {
                if(!graph.containsKey(i)) {
                    graph.computeIfAbsent(i, ArrayList::new).add(edges[i]);
                }
                else {
                    graph.get(i).add(edges[i]);
                }
            }
        }
        return graph;
    }

    public HashMap<Integer, Integer> doBFS(int start, HashMap<Integer, ArrayList<Integer>> graph) {
        int i = 1;
        HashMap<Integer, Integer> level = new HashMap<>();
        HashMap<Integer, Integer> parent = new HashMap<>();
        level.put(start, 0);
        parent.put(start, null);
        ArrayList<Integer> frontier = new ArrayList<>();
        frontier.add(start);
        while(frontier.size() > 0) {
            ArrayList<Integer> next = new ArrayList<>();
            for(int u : frontier) {
                if(graph.containsKey(u)) {
                    for(int v : graph.get(u)) {
                        if(!level.containsKey(v)) {
                            level.put(v, i);
                            parent.put(v, u);
                            next.add(v);
                        }
                    }
                }
            }
            frontier = next;
            i++;
        }
        return level;
    }

    public static void main(String[] args) {
        BFS result = new BFS();
        int[] edges = new int[]{2,2,3,-1};
        HashMap<Integer, ArrayList<Integer>> graph = result.edgesToGraph(edges);
        System.out.println(result.doBFS(0, graph));
    }
}
