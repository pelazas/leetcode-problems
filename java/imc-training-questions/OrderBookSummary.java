import java.util.Collections;
import java.util.Map;
import java.util.TreeMap;

public class OrderBookSummary{
    private final TreeMap<Double, Long> bids = new TreeMap<>(Collections.reverseOrder());
    private final TreeMap<Double, Long> asks = new TreeMap<>();

    public void addOrder(String side, double price, long quantity){
        TreeMap<Double, Long> book = side.equalsIgnoreCase("bid") ? bids : asks;
        if (!book.containsKey(price)){
            book.put(price, quantity);
        } else{
            long old_volume = book.get(price);
            book.put(price, old_volume + quantity);
        }
    }

    public void printMarketSnapshot(){
        Map.Entry<Double, Long> bestBid = bids.firstEntry();
        Map.Entry<Double, Long> bestAsk = bids.firstEntry();

        if(bestBid != null){
            System.out.println("Best bid: "+ bestBid.getValue() + " @ " + bestBid.getKey());
        }
        if(bestAsk != null){
            System.out.println("Best ask: "+ bestAsk.getValue() + " @ " + bestAsk.getKey());
        }
    }

}