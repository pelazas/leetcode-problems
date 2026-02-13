import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;

public class OrderGateway {
    // lots of orders/sec, assign unique ID, and put in line to be processed by a consumer engine
    
    // thread safe counter for IDs
    private final AtomicInteger orderIdGenerator = new AtomicInteger(0);

    // thread safe queue: 1000 orders capacity
    private final BlockingQueue<Order> processingQueue = new LinkedBlockingQueue<>(1000);
    

    public void submitOrder(String symbol, int qty){
        int id = orderIdGenerator.incrementAndGet();
        Order newOrder = new Order(id, symbol, qty);
        try{
            processingQueue.put(newOrder);
        } catch (InterruptedException e){
            Thread.currentThread().interrupt();
        }
    }
    // called by consumer threads
    public void processOrders(){
        while(true){
            try{
                Order o = processingQueue.take();
                executeOrder(o);
            } catch(InterruptedException e){
                Thread.currentThread().interrupt();
            }
        }
    }

    private void executeOrder(Order o){
        System.out.println("Executing order with id:"+o.id);
    }
    
}

class Order {
        final int id;
        final String symbol;
        final int qty;

        Order(int id, String symbol, int qty) {
            this.id = id;
            this.symbol = symbol;
            this.qty = qty;
        }
    }